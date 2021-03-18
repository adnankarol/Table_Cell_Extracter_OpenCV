# Coding Round for Just Add AI GmbH
Implementation of Cell Extractor from Images of Tables.


# Table of Contents
1. [ To Run. ](#Using)
2. [ Output. ](#Output)
3. [ Additional Packages. ](#Packages) 
4. [ Python Version. ](#Version) 
5. [ Future Scope. ](#Future_scope)
6. [ Additional Information. ](#info)

<a name="using"></a>
# To Run

1.  Open command line cmd at the root of the repository.

2.  Run the command   

    `pip install -r requirements.txt` 

3. Follow Point 4 for tesseract installation. Without `tesseract.exe` empty cells will also be saved by default.

4. Run the command 

    `python extract_cells.py`

NOTE:  In order to make path or any related change, please change the `config.yaml` file. 


<a name="Output"></a>
# Output

## Output Cells Images
Output for Each Image is saved in a seperate folder with image name under results folder in the format as given below.


        results/image_name/cell_RowNumber_ColumnNumber.png


Example Output Format

        results/0/cell_0_2.png

## Json Output
There is also a `output.json` file that is stored under `results` folder that stores each cell cordinate in format (x, y, w, h) along with the image name.

<a name="Packages"></a>
# Additional Packages

In order to NOT add empty cells, the program uses package called `pytesseract` from python which has to be installed in the following ways as given below.

1. Download the tool from [here](http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe).

2. Run the installer with default settings.

2. Open the location for `tesseract.exe` which should be saved in the C drive under program files such as `C:\Program Files\Tesseract-OCR`. Copy the location.

3. Add to path variables. Windows search bar -> Edit environment variables for your account -> Click Path -> Click Edit -> Click New -> Paste Location for `tesseract.exe` -> Click OK -> Click OK.

4. Finally `pip install pytesseract` at command prompt window.

5. To Confirm . Open command prompt and type `tesseract`, which should NOT give an Error and show several further commands.

6. Hooray!! Now we have OCR package confirmed. 

NOTE : Without `tesseract.exe` empty cells will also be saved by default.

<a name="Version"></a>
# Python Version
The whole project was developed on Python Version `Python 3.8.1` and Pip Version `pip 21.0`.

<a name="Future_scope"></a>
# Future Scope

1. Use of OCR system to extract data from these image using some packages like tesseract from python.

2. Using AI and Deep Learning to convert the image data to text.

<a name="info"></a>
# Additional Information
In case of error, feel free to contact me over Linkedin at [Adnan](https://www.linkedin.com/in/adnan-karol-aa1666179/).
