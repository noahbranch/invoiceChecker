import aspose.words as aw

doc = aw.Document('1402.pdf')

save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)
save_options.page_set = aw.saving.PageSet(0)
doc.save("1402Pdf.png", save_options)