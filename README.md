# CalcularDV - Postal Label Check Digit Calculator

<p align="center"><img src="./static/imagens/logo2.png">
</p>

A python software to calculate the digit checker of postal labels.

## Install

Installation is very easy. Download this project, create a virtual environment and install the dependencies below.

### Dependencies

- PyGObject
- GTK3
  For instructions on how to install these dependencies go to the link: [PyGObject](https://pygobject.readthedocs.io/en/latest/getting_started.html)

## Usage

Run the app. On the home screen enter the eight numeric digits of the postal label.

The international standard for postal labels follows the model:

**AB123456789CD**

The first two letters usually refer to the type of service contracted. These letters should be ignored.

The ninth digit is a check digit. It's obtained through a calculation performed with the first eight digits.

The final two letters usually refer to the country where the package was posted. These two letters are also ignored.

Enter the first eight digits in the input field and click calculate.

The check digit will appear next.

## Create a .exe for Windows

## License

CalcularDV is licensed under the GNU General Puclic License v3.0. See [LICENSE](https://github.com/jeffyuri7/calcularDV/blob/main/LICENSE) for more details.
