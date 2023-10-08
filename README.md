LaTeX-Based CV
============================

<div align="center">
  <img src="assets/images/cv-preview.png" alt="CV Preview">
</div>

Prerequisites
-------------

To successfully compile and build this CV project, please ensure the following prerequisites are met:

### Version Control: Git LFS

Install Git Large File Storage (LFS) to properly download the included icons, fonts, and images:

```bash
git lfs install
```

### LaTeX Installation

Ensure that the LaTeX tools are installed. For macOS, execute the following command:

```bash
brew install texlive
```

### Ghostscript for PDF Compression

To enable PDF compression, Ghostscript (gs) needs to be installed:

```bash
brew install ghostscript
```

### Font Management

For optional icon support (e.g., GitHub, LinkedIn), install the FontAwesome font system-wide. Locate the font file at `assets/fonts/FontAwesome.otf`.

If you encounter font-related issues, consider installing the fonts systemwide. I had issues with this font: `Acumin-BdPro.otf`.

Adding New Logos
----------------

Icons should be placed in the `assets/logos` folder.
I've developed a Python script for automated icon image adjustment. The script crops and resizes icon images into square shapes. PNG files without a background are recommended for optimal results.

### Pillow Library

The script utilizes the Pillow image processing library. Install it via pip:

```bash
pip install Pillow
```

### Running the Script

Execute the script as follows:

```bash
python scripts/logo-crop-script.py --input_folder assets/to_convert --output_folder assets/converted --size 1200
```

This will process all images in the `input_folder` and output them to `output_folder` at the specified size (px). The resulting images can then be seamlessly integrated into the document.

PDF Compilation
---------------

### Building the PDF

Compile the LaTeX document into a PDF using the following command:

```bash
latexmk -synctex=1 -interaction=nonstopmode -file-line-error -xelatex main.tex
```

### Compressing the PDF

To reduce the PDF file size to a more manageable level, use:

```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH -sOutputFile=vincent_cv.pdf main.pdf
```

### Language

To Build the PDF in english, change the selected language in `src/selected_language.tex` to english / german.

### Makefile for Automation

All aforementioned commands can be executed via the `Makefile`.  
For example Simply run:

```bash
make pdf
```

to generate a compressed PDF of your CV.

Github Actions
--------------

This repository will automatically build the pdfs in english and german and create a release, it will keep the 5 most current releases.
It will also upload the pdfs to a server to host the cvs online as a direct download.
