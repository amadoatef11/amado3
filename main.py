from flet import *
import sys
import codecs

# Ensure your encoding is set to 'utf-8'
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Your code logic here

def main(page:Page):
    T = Text('Rakwan ali')
    page.add(T)
    
    page.update()

app(main)
