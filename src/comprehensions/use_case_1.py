

def center_text(*args):
    text = '-'.join([str(arg) for arg in args])
    left_margin = (80 - len(text)) // 2
    print(' ' * left_margin, text)


center_text('Spam and Eggs')
center_text(12)
center_text('First', 'Second', 3, 4, 'Spamm')