from googletrans import Translator
translator = Translator()
text = input("Enter Text:")
language=input("select language : ")
translated=translator.translate(text,dest=language)
print("Original Text:", text)
print("Translated Text:", translated.text)
