# Tone Enhancement

Enhance contrast in image by seperating it into base and detail layers with some modifications then merge them back.


## Usage

- Make directories: `input` and `output`
- Put all your images in the `input` folder
- Execute the program

    ```bash
    python main.py {method_name: `BF` | `L0`}
    ```
- All the results will show wih window displaying and save in `output`


## Method

Here are two decomposition methods implemented in this project,

- Bilateral Filtering, implemented by OpenCV
- L0 smoothing, and implementation comes from [L0 gradient minimization](https://github.com/t-suzuki/l0_gradient_minimization_test)

## Result

- Source input

    ![](sample/src/IMAG0237.jpg)

    ![](sample/src/hdr1.jpg)

- With bilateral filtering

    ![](sample/BFIMAG0237.jpg)

    ![](sample/BFhdr1.jpg)

- With L0

    ![](sample/L0IMAG0237.jpg)

    ![](sample/L0hdr1.jpg)
