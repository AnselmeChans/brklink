#brkink

### A Python library that browses all the links contained in a web page and displays the broken links.

#### Author: Hans CERIL

#### License: MIT

## download and install

1. Under the repository name, click to copy the clone URL for the repository. ![](https://help.github.com/assets/images/help/repository/clone-repo-clone-url-button.png)

2. Clone your project : Go to your cumputer's shell and type the following command: `git clone < Paste HTTPS OR SSH Here > `

2. Go to the location where you want the cloned directory to be made:  `cd <PathWhereIWantToClone>`

3. To easily install Python packages : `sudo python requirements.txt install`

## development

La commande aura les options suivantes :
  - help : affiche l’usage de la commande
  - depth = n : profondeur de recherche n (1 par défaut)

## executable

  python3 brklink -h

   python3 brklink -d <depth> <url>

   ou

   python3 brklink --depth <depth> <url>
