from manim import *

class LinearSearch(Scene):
    def construct(self):
        # Array and target
        arr = [3, 7, 2, 9, 5, 1]
        target = 9

        # Create array boxes
        boxes = VGroup()
        numbers = VGroup()

        for i, value in enumerate(arr):
            box = Square(side_length=1)
            box.move_to(RIGHT * i * 1.2)
            num = Text(str(value), font_size=36)
            num.move_to(box.get_center())

            boxes.add(box)
            numbers.add(num)

        array_group = VGroup(boxes, numbers)
        array_group.center()

        # Target text
        target_text = Text(f"Target = {target}", font_size=36)
        target_text.to_edge(UP)

        self.play(Create(boxes), Write(numbers), Write(target_text))
        self.wait(1)

        # Linear search
        for i, value in enumerate(arr):
            self.play(boxes[i].animate.set_fill(YELLOW, opacity=0.5))
            self.wait(0.5)

            if value == target:
                self.play(boxes[i].animate.set_fill(GREEN, opacity=0.7))
                found_text = Text(f"Found at index {i}", font_size=36, color=GREEN)
                found_text.to_edge(DOWN)
                self.play(Write(found_text))
                self.wait(2)
                return
            else:
                self.play(boxes[i].animate.set_fill(WHITE, opacity=0))
