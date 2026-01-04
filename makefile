# expects a parameter called md
# usage: make slide md=filename

MARKDOWN_FOLDER = ./markdown
BUILD_FOLDER = ./build
OUTPUT_FOLDER = ./slides

slide:
	cp $(MARKDOWN_FOLDER)/$(md).md $(BUILD_FOLDER)
	python3 src/ml/utils/image_paths.py $(BUILD_FOLDER)/$(md).md  
	pandoc -t beamer $(BUILD_FOLDER)/$(md).md -o $(OUTPUT_FOLDER)/$(md).pdf	

all-slides:

	@for file in $(wildcard $(MARKDOWN_FOLDER)/*.md); do \
		filename=$$(basename $$file); \
		filename_no_ext=$${filename%.*}; \
		cp $$file $(BUILD_FOLDER); \
		python3 src/image_paths.py $(BUILD_FOLDER)/$${filename}; \
		pandoc -t beamer $(BUILD_FOLDER)/$${filename_no_ext}.md -o $(OUTPUT_FOLDER)/$${filename_no_ext}.pdf; \
		echo $$filename_no_ext; \
	done
clean:
	rm build/* 


