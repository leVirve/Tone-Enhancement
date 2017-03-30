import os
import glob

import cv2

from photo import Photo, adjust_gamma, clach


def main(method_name):
    for file in glob.glob('input/*.jpg'):
        photo = Photo(os.path.basename(file), scale=0.2)

        base, detail = photo.spilt_layers(method_name)

        l_scale = 0.87
        base *= l_scale
        base = clach(base)
        base = adjust_gamma(base, gamma=1.1)
        base /= l_scale

        detail_g = cv2.GaussianBlur(detail, (3, 3), 2.0)
        detail = cv2.addWeighted(detail, 1.5, detail_g, -0.5, 0, detail)

        output = base + detail * 1.5
        output = output.clip(0, 1) * 255

        cv2.imshow('img', (photo.img * 255).astype('uint8'))
        cv2.imshow('output', output.astype('uint8'))
        cv2.waitKey()
        photo.save_img(output.astype('uint8'), method_name=method_name)


if __name__ == '__main__':
    main('L0')
