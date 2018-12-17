# encoding:utf-8
import re


def format_contents(path, title):
    with open(path, 'rb') as f:
        title_pat = r'^第 *([\d]*) *章 (.*) [\d]*$'
        text_pat = r'^([\d\.]*) (.*) ([\d]*)$'
        contents_list = [title]  # 目录列表
        for line in f:
            line = line.decode('utf-8').strip().replace('*', '第')
            title_match = re.match(title_pat, line)
            if title_match:  # 一级标题
                level_tmp = 1
                value = '第' + \
                    title_match.group(1) + '章 ' + title_match.group(2)
            else: # 其他标题
                text = re.match(text_pat, line)
                level_list = text.group(1).split('.')
                level_tmp = len(level_list)
                value = level_list[-1] + ' ' + text.group(2)
            if level_tmp > 2: # 跳过深度大于 2 的标题
                continue
            contents_list.append(' ' * level_tmp * 4 + value + '\n')
    return contents_list


if __name__ == "__main__":
    path = './Contents/Linux Shell 脚本攻略.txt'
    write_path = path[:-4] + '_Contents.txt'
    contents = format_contents(path, title='Linux Shell 脚本攻略\n')
    with open(write_path, 'w', encoding='utf-8') as f:
        f.writelines(contents)
