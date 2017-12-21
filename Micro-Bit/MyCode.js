input.onGesture(Gesture.Shake, () => {
    for (let i = 0; i < 4; i++) {
        basic.showNumber(Math.random(7))
        basic.pause(100)
    }
})
basic.forever(() => {
    music.ringTone(input.compassHeading())
    basic.showArrow(ArrowNames.North)
    basic.clearScreen()
    basic.pause(100)
    basic.showNumber(input.temperature())
})
