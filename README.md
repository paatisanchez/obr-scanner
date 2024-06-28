# OBR Scanner Tool

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Description

A Python script that monitors a specified directory for file creation or modification events using the `watchdog`
library.\
When events occur, it runs a script `run_local.py` and starts a scanner software specified by the `scanner_exe`
environment variable.

## Table of Contents

- [Documentation](#documentation)
- [Requirements](#requirements)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Installation Steps](#installation-steps)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Documentation

Explore project documentation and manuals in the [Documents](Documents) directory:

- [Description Manual (Word)](Documents/Description_Manual.docx)
- [Description Manual (PDF)](Documents/Description_Manual.pdf)

Learn about the frame and its construction:

- [Frame Documentation (Word)](Documents/Frame.docx)
- [Frame Documentation (PDF)](Documents/Frame.pdf)

## Requirements

- Python 3.x
- `watchdog` library: Install it using `pip install watchdog`

## Dependencies

This project relies on the [AngelinaReader](https://github.com/IlyaOvodov/AngelinaReader) GitHub repository. Ensure it
is installed and running before using this script.

Follow the installation instructions for the [AngelinaReader](https://github.com/IlyaOvodov/AngelinaReader) in its
repository.

## Installation

- Python 3.x
- `watchdog` library: Install it using `pip install watchdog`

## Installation Steps

1. Set up the environment:
    - Ensure you have Python installed.
    - Install the required Python packages by running:
   ```bash
   pip install watchdog
   ```

2. Set the `scanner_exe` environment variable:
    - Specify the path to the scanner software executable in the environment variable.
       - Open Command Prompt with administrative privileges:
  ```cmd
  setx scanner_exe "C:\path\to\scanner.exe"
  ```

## Usage

### OBR Scanner


Run the script:

   ```bash
   python app.py
   ```

The file app.py has to be inside the [AngelinaReader](https://github.com/IlyaOvodov/AngelinaReader) repository,
otherwise it doesn't work

### Document Comparison
- The **compare-documents** folder houses essential tools for comparing scanned documents with their original versions.     
- This functionality enables users to evaluate the accuracy of the scanning process by identifying disparities between the scanned and original documents.     
- For detailed instructions on utilizing these tools, please refer to the corresponding README within the [compare-documents](/compare-documents/README.md) folder.

### Usage of the scanner

Manual:

1.	For scanning turn on the scanner by pressing the button on the back of the scanner. Make sure to turn on the light by pressing the button on the front right. 
2.	If correctly connected to the pc, the program should recognize the scanner and show the camera view. 
3.	By pressing the button scan it takes a picture of the paper. 
4.	The doc should be saved in a folder called “input” . Check the date to make sure it is the right scan. You can also go directly to the folder from the program 


For centralization: 
- Open Box
- Put the two blocks in the holes on the plate
  ![image](https://github.com/paatisanchez/obr-scanner/assets/162608488/f3d61505-6c45-41a7-8cfd-22473bd29cea)
![image](https://github.com/paatisanchez/obr-scanner/assets/162608488/d2cfe89b-2aa6-4b24-a93d-e9fe0e188419)

- Choose appropriate plate for paper size 
- Position the plate on the blocks  with the grooves
  ![image](https://github.com/paatisanchez/obr-scanner/assets/162608488/f5f3dacc-a5d6-45c1-a6a4-9fa718ec8358)

- Put paper on top
  ![image](https://github.com/paatisanchez/obr-scanner/assets/162608488/66b0f671-26ea-4359-a010-60fe59cdb13a)

- The paper should be centered

## Accesibility 

### CZUR Accesibility

- For Mac users:
    - **VoiceOver**: The integrated screen reader VoiceOver works seamlessly with CZUR scanner.
  
- For Windows users:
    - **Commands for Scanning**: There are already developed commands to initiate scanning without needing a screen reader.
        - alt + k: rotate
        - alt + y: cancel
        - alt + u: reset
        - alt + b: scan
        - alt + p: print
          
## Configuration

Modify the `watch_directory` variable in the script to specify the directory to monitor.
Adjust the `language` variable and the script command in the `Handler` class to fit your requirements.

## Notes

This script assumes a Unix-like environment.
If your operating system is windows set up the environment variable accordingly.

## Contributing

If you would like to contribute to the project, provide guidelines for how others can do so. This may include
information about submitting bug reports, feature requests, or code contributions.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [AngelinaReader](https://github.com/IlyaOvodov/AngelinaReader)
