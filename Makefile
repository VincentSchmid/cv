build:
	-latexmk -synctex=1 -interaction=nonstopmode -file-line-error -xelatex -outdir=build src/main.tex

compress:
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH -sOutputFile=vincent_cv.pdf build/main.pdf

icons:
	python scripts/logo-crop-script.py --input_folder assets/to_convert --output_folder assets/converted --size 1200

pdf: build compress
