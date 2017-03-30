import cv2
import numpy as np

from l0_gradient.l0_gradient_minimization import l0_gradient_minimization_2d


class Photo():

    input_dir = 'input/'
    output_dir = 'output/'

    methods = {
        'BF': {
            'func': cv2.bilateralFilter,
            'args': {'d': 9, 'sigmaColor': 9, 'sigmaSpace': 50}
        },
        'L0': {
            'func': l0_gradient_minimization_2d,
            'args': {'lmd': 0.02, 'beta_max': 1.0e5, 'beta_rate': 2.0}
        }
    }

    def __init__(self, filename, scale=None):
        self.filename = filename
        self.img = self.load_img(self.input_dir + filename, scale)
        self.normalize()

    def get_algo(self, method):
        algo = self.methods[method]
        return algo['func'], algo['args']

    def spilt_layers(self, method='BF'):
        func, kwargs = self.get_algo(method)
        base = func(self.img, **kwargs)
        detail = self.img - base
        base = self.img - detail
        return base, detail

    def load_img(self, filepath, scale):
        img = cv2.imread(filepath)
        if scale:
            h, w = np.dot(img.shape[:2], scale).astype(np.int)
            img = cv2.resize(img, (w, h))
        return img

    def normalize(self):
        self.img = np.array(self.img, dtype=np.float32)
        self.img /= 255

    def save_img(self, data, method_name='BF'):
        return cv2.imwrite(self.output_dir + method_name + self.filename, data)


def adjust_gamma(img, gamma=1.0):
    return img ** (1.0 / gamma)


def clach(img):
    ''' Contrast Limited Adaptive Histogram Equalization '''
    ycc = cv2.cvtColor(img.astype('float32'), cv2.COLOR_BGR2YCR_CB)
    clahe = cv2.createCLAHE(clipLimit=1.2, tileGridSize=(8, 8))
    y = ycc[:, :, 0].clip(0, 1)
    ycc[:, :, 0] = clahe.apply((y * 255).astype('uint8')).astype('float32') / 255
    return cv2.cvtColor(ycc, cv2.COLOR_YCR_CB2BGR)
