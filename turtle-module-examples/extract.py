import colorgram as cg


class color_extract:

    def extract_colors(self):

        color_list = cg.extract("hirst.jpg", 30)
        color_palette = []

        for i in range(len(color_list)):
            r = color_list[i].rgb.r
            g = color_list[i].rgb.g
            b = color_list[i].rgb.b
            new_color = (r, g, b)
            color_palette.append(new_color)

        return color_palette
