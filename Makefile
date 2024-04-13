german:
	echo "\def\mylanguage{german}" > src/selected_language.tex

english:
	echo "\def\mylanguage{english}" > src/selected_language.tex

build-tex:
	latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdfxe -outdir=build src/main.tex

compress:
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH -sOutputFile=vincent_cv.pdf build/main.pdf

icons:
	python scripts/logo-crop-script.py --input_folder assets/to_convert --output_folder assets/converted --size 1200

pdf: build-tex compress

pdfs:
	make german
	make pdf
	mv vincent_cv.pdf vincent_cv_de.pdf
	make english
	make pdf
	mv vincent_cv.pdf vincent_cv_en.pdf
