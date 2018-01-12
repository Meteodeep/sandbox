input.onButtonPressed(Button.A, () => {
    basic.showNumber(input.compassHeading())
    if (input.compassHeading() <= 90) {
        basic.pause(100)
        images.createImage(`
            # # # # #
            # . . . .
            # # # . .
            # . . . .
            # # # # #
            `).showImage(0)
    } else {
        if (input.compassHeading() <= 180) {
            basic.pause(150)
            images.createImage(`
                . # # # #
                # . . . .
                . # # # .
                . . . . #
                # # # # .
                `).showImage(0)
        } else {
            if (input.compassHeading() <= 270) {
                basic.pause(150)
                images.createImage(`
                    # . . . #
                    # . . . #
                    # . # . #
                    . # . # .
                    . # . # .
                    `).showImage(0)
            } else {
                if (input.compassHeading() <= 360) {
                    basic.pause(150)
                    images.createImage(`
                        # . . . #
                        # # . . #
                        # . # . #
                        # . . # #
                        # . . . #
                        `).showImage(0)
                }
            }
        }
    }
})
