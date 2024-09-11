# Setup
This project can be executed using any integrated development environment (IDE) that supports Python and Jupyter Notebook. \
[Visual Studio Code](https://code.visualstudio.com/) is recommended.

## Basic Requirements:
- [Python](https://www.python.org/downloads/)
- [Jupyter Notebook](https://jupyter.org/)
- [pandas](https://pandas.pydata.org/)

## VS Code Setup
1. Install [Visual Studio Code](https://code.visualstudio.com/Download)
2. Install [Python](https://apps.microsoft.com/search/publisher?name=Python+Software+Foundation) from the Microsoft Store.
3. Install the necessary extensions
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
4. Install Required Libraries using pip
   - Press ``Ctrl+\` `` (backtick) or `` Cmd+\` `` (backtick) to open the integrated terminal.
   - Install pandas using the following code:
   ```bash
   python pip install pandas
   ```
   - To check if the package was installed successfully, you can run the following command:
   ```bash
   python pip show pandas
   ```
   This will display information about the installed pandas package, including its version and location.
5. Add the chatbot folder into the _VS Code Explorer_ (`Ctrl+E`).