<img height="20px"  src="https://i.imgur.com/1ubgfmC.png"><a href="README-pt-br.md"> – Leia em português!</a><br/>
<img height="20px"  src="https://i.imgur.com/UrpOBOr.png"><a href="README.md"> – Read in English!</a>
------------------------------------------------------------
# Snes Game Manager


 
  SGM is an application that aims to organize roms of your Super Nintendo emulator in a visual, simple and practical way.  
Some of the application's functions include:
* Detect rom files and arrange them in a ordered list.
* Download game covers automatically, based on the name of the game.
* Run the rom on your favorite emulator.

## Installation

### Executable
For now, the executable version of SGM is only compatible with linux.  
Available for download [here](https://drive.google.com/file/d/1fCHrqvh0bogIbvInQLTkmPVjFTGgjGNI/view?usp=sharing).  
After unpacking the file. Provide the necessary permissions for the SGM executable located in the root directory.    
For now SGM is only compatible with the zsnes emulator. So be sure to download it with:  

(ubuntu)

```bash
sudo apt install zsnes
```
### Python
For a more versatile version, use SMG direct from python.  
This version has not been tested yet. But most likely works on windows and mac.  
Make sure you have python 3.6 installed with "PyQt5" and "requests" libraries on your computer.  
Unzip the downloaded project from the [github](https://github.com/allanvobraun/SnesGameManager) page. 
 Then run main.py with:

```bash
python3.6 main.py
```

## Usage
When running the program this will be the main screen.  
Click "File" and then "Open roms folder" to add your roms folder.  

![passo1](https://i.imgur.com/697bgOA.png)
  

A window should open as the file browser, select the desired folder and click "open".  

![passo2](https://i.imgur.com/934gK4T.png)
  

After this the files will be loaded and organized.  
To download the game covers, click on "Functions" and then "Download game covers".  

![passo3](https://i.imgur.com/qHYPUxB.png)
  

The download will start, after its completion close the dialog box.  
Note that sometimes a cover download can fail. 
This is probably due to the ROM file name.   
Try to modify it to be compatible with the original name of the game in capitalized letters.    

![passo4](https://i.imgur.com/ZZfPKQk.png)

  
To play the game, simply select it and hit the Play button. Your emulator should take care of the rest.

## Future additions
In future versions SGM will bring features like:
* Support for Windows and Mac OS.
* Support for other emulators like higan and snes9x.
* Function for configuring controls and shortcuts.
* Support for Japanese game covers.
* Carousel display function.
* Function to better configure the game list.

## Project Structure
The project is written in python 3.6, using the UI library PYQT5.  
The UI was built entirely using the QT designer.  
In order to "compile" the project in executable form, the [pyinstaler](https://www.pyinstaller.org/) was used.  
In order to download the images, the python requests library was used.    
All images are downloaded from this amazing [repository](https://github.com/ZeroSuf3r/nintendo-games-icons).  
The code is all appropriate for the English language, although the comments are written in pt-br.
 This should not be a big obstacle, but I will try to translate that part into the future.
 



## Contributing
Pull requests are welcome. For big changes, please open a issue to discuss the change.  
For direct contact, send me an e-mail: allanvobraun@gmail.com
## License
Free Software.  
[MIT](https://choosealicense.com/licenses/mit/)