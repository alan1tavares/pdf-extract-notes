import fitz;

doc = fitz.open("a.pdf");

import fitz

for page in doc:
	for annot in page.annots():
		# print(f'Page: {page.number} - {page.get_textbox(annot.rect)}\n')
		print(f'Annotation on page: {page.number} with type: {annot.type} and rect: {annot.rect} - {annot.info} - {annot.get_textbox(annot.rect)}')