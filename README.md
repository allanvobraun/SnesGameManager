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

### Linux

If you are using a debian-based linux distribution, download the .deb version from [releases](https://github.com/allanvobraun/SnesGameManager/releases/download/1.0/sgm_1.0_all.deb) and run the file with your favorite package installer. This should install sgm without difficulty.

If you prefer, there is a flatpak version available [here](https://github.com/allanvobraun/SnesGameManager/releases/download/1.0/sgm_1.0_64x.flatpak) for all linux distributions with flatpak package support.  
However the flatpak version requires internet connection to download dependencies, being common a slow installation.  
Before you begin the installation, make sure that flatpak is installed on your computer by entering the following command on a terminal:

```bash
flatpak --version
```

If the output to the command **does not** show the version of flatpak, make sure that flatpak is installed on your computer.  
Proceeding type:

```bash
flatpak install path/to/file/sgm_1.0_64x.flatpak
```

After that accept the installation of the packages and enter your root password when needed.  
After installation (it is often slow) locate the .desktop file that was created and then open it (it is also common to take a few seconds to open).  
installation completed!

### Windows

You can install sgm on windows with a simplified installer [here](https://github.com/allanvobraun/SnesGameManager/releases/download/1.0/sgm_windows_1.0.exe).  
Simply run the installer and follow the steps in the screen.


You can also can download the .zip version of sgm.
If this is the case extract the files in the desired folder and run the file "sgm.exe" to open the application.


## Usage
When running the program this will be the main screen.  
Click "File" and then "Open roms folder" to add your roms folder.  

![passo1](https://i.imgur.com/yCnvfU9.png)
  

A window should open as the system file browser, select the folder where your super nintendo roms are stored. 

![passo2](https://i.imgur.com/xTnTeZJ.png)
  

After that the files will be loaded and organized.  
To download the game covers, click on "Functions" and then "Download game covers".  

![passo3](https://i.imgur.com/0lpWDuA.png)
  

The download will start, after its completion close the dialog box.  
Note that sometimes a cover download can fail. 
This is probably due to the ROM file name.   
Try to modify it to be compatible with the original name of the game, make use of capitalized letters.    

![passo4](https://i.imgur.com/JTslF16.png)

  
You need to have an emulator installed on your computer, [Zsnes](https://www.zsnes.com/), [Higan](https://higan.byuu.org/) and [snes9x](http://www.snes9x.com/) are good choices.  
Now is the time to configure your emulator.  
Click "Settings" and then select "Emulator Configuration".  
If you are using sgm on any linux distribution, sgm will store the shell commands of the emulators: Zsnes, Higan and Snes9x automatically.  
Then select the desired emulator or set your own in the "custom" option. After finishing press "Apply".

![passo5linux](https://i.imgur.com/BfpDXe7.png)

If you are using the Windows version, you should click the "..." button to search with file explorer for the executable bin of a emulator.  
Just like Linux version you can select any other emulator with the "custom" option.  
After finishing select your default emulator and then press "Apply".

![passo5windows](https://i.imgur.com/HcljO94.png)

To play a game, simply select it and press the Play button. Your default emulator should start the game.  
Either, just right click on the game to select a specific emulator.

### Extra

If you want to change the aspect of the application, Breeze Dark and Breeze Light themes are available in the linux version.  
However in the Windows version only the theme Breeze Dark is functional for now.

To change the theme, in the main window press "Settings" and then select "Change theme".
Here you can change the theme and see a small preview, after finishing click "Apply".

## Future additions
In future versions SGM will bring features like:

* Bug notification system and warnings.
* Function for configuring controls and shortcuts.
* Support for Japanese game covers.
* Carousel display function.
* Function to better configure the game list.

## Project Structure
The project is written in python 3.6.8, using the UI library PYQT5.  
The UI was built entirely using the QT designer.  
In order to "compile" the project in executable form, the [pyinstaler](https://www.pyinstaller.org/) was used.  
The flatpak version does not use pyinstaller.  
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