import colors, random


def draw_letter(x_letter, x_color, x_screen, x_font, xy_list):
    text_surface = x_font.render(x_letter, True, x_color)
    x_screen.blit(text_surface, (xy_list[0], xy_list[1])) 


def draw_time(x_time, x_screen, x_font, window):
    text_surface = x_font.render(x_time, True, colors.STATS)
    x_screen.blit(text_surface, (window[0] - 100, 20)) 


def get_wpm(x_text, x_time):
    x_time = x_time / 60
    wpm = round((len(x_text) / 5) / x_time)
    return wpm


def get_pec(in_text, out_text):
    correct = 0
    for i, s in enumerate(in_text):
        if s == out_text[i]:
            correct += 1
    percentege = round(correct / len(in_text) * 100)
    return percentege


def draw_result(x_wpm, x_percentege, x_screen, x_font):
    wpm_surface = x_font.render(str(x_wpm) + "wpm", True, colors.STATS)
    percentege_surface = x_font.render(str(x_percentege) + "%", True, colors.STATS)

    x_screen.blit(wpm_surface, (20, 20)) 
    x_screen.blit(percentege_surface, (300, 20)) 


def get_text(x_text):
    x_text = x_text.split(" ")
    random.shuffle(x_text)

    return " ".join(x_text)