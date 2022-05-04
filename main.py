from pyautogui import center, locateOnScreen, click

def click_a_pic(path):
    button = None
    while button is None:
        button = locateOnScreen(path, confidence=0.9)
    buttonCoords = center(button)
    click(buttonCoords[0], buttonCoords[1])

def main() -> None:

    embarkPic = 'Buttons/embark.png'
    tokenPic = 'Buttons/token.png'
    retirePic1 = 'Buttons/retire.png'
    retirePic2 = 'Buttons/retire2.png'
    continuePic = 'Buttons/continue.png'
    
    clickSequence = [embarkPic, tokenPic, retirePic1, retirePic2, continuePic, continuePic]
    iterations = 86

    for tokens in range(0, iterations+1):
        for path in clickSequence:
            click_a_pic(path)
        print(f"tokens remaining: {iterations - tokens - 1}")

if __name__ == "__main__":
    main()