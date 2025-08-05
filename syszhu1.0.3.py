import getpass
from datetime import datetime  # 导入datetime模块以获取当前时间
import platform  # 用于获取系统信息
import random    # 用于生成随机数
import sys       # 用于获取Python版本信息
import os        # 用于清屏命令和文件操作
import webbrowser  # 用于打开浏览器
from collections import defaultdict
from datetime import datetime, timedelta
import random
import string
from ftplib import FTP
import time
# 账号密码信息
accounts = {
    'admin': 'admin',
    'visit': 'visit123',
    'feng': 'fakefake123'
    #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
}

# 命令历史记录列表
command_history = []

def errorno():
    print("正在收集错误信息...")
    try:
        webbrowser.open('http://yigestudio-great.com')
        print("成功发送错误信息。")
    except Exception as e:
        print(f"尝试发送错误信息时出错: {e}")

def dtsys():
    print("宜鸽工作室©赵丛瑞 版权所有 版本v1.0.0_2025-02-23_02587 ")
   
    
def generate_password():
    try:
        length = int(input("请输入密码长度（建议不少于8位）：") or 12)
        if length < 4:
            print("错误：密码长度过短，建议至少4个字符")
            return
#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        include_lower = input("是否包含小写字母？(y/n): ").lower() == 'y'
        include_upper = input("是否包含大写字母？(y/n): ").lower() == 'y'
        include_digits = input("是否包含数字？(y/n): ").lower() == 'y'
        include_special = input("是否包含特殊字符？(y/n): ").lower() == 'y'

        selected_chars = ''
        if include_lower:
            selected_chars += string.ascii_lowercase
        if include_upper:
            selected_chars += string.ascii_uppercase
        if include_digits:
            selected_chars += string.digits
        if include_special:
            selected_chars += string.punctuation

        if not selected_chars:
            print("错误：必须至少选择一种字符类型")
            return

        password = ''.join(random.choice(selected_chars) for _ in range(length))
        print(f"生成的密码是: {password}")
    except ValueError as e:
        print(f"错误: {e}")

    
def show_time():
    print(f"当前日期时间是 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def connect_to_ftp(host, port, user, passwd):
    try:
        # 创建一个新的 FTP 对象并连接到指定主机和端口
        ftp = FTP()
        ftp.connect(host=host, port=port)
        #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        # 打印欢迎信息
        print(ftp.getwelcome())
        
        # 登录到 FTP 服务器
        ftp.login(user=user, passwd=passwd)
        print("登录成功，开始使用线上服务")
        
        return ftp
    
    except Exception as e:
        print(f"连接或登录失败: {e} 正在使用离线系统")
        return None
        

# 定义 FTP 服务器信息
ftp_host = '192.168.1.50'  # 替换为实际的 FTP 服务器地址
ftp_port = 2121          # 默认端口，如果不是默认端口，请替换为你需要使用的端口号
ftp_user = '12'    # 替换为你的用户名
ftp_pass = '123'    # 替换为你的密码

# 使用示例
ftp_connection = connect_to_ftp(ftp_host, ftp_port, ftp_user, ftp_pass)

def help_command():
    print("可用命令如下：")
    for cmd, (_, desc) in commands.items():
        print(f"{cmd} - {desc}")

def private_space(username):
    print(f"欢迎来到{username}的隐私空间，隐私空间内无法使用任何功能，需要输入[当前用户]:[当前密码]以退出")
    while True:
        exit_code = input("请输入当前登录的用户名和密码以退出隐私空间：").strip()
        if exit_code == f"{username}:{accounts[username]}":
            break
        else:
            print("不能使用此指令")
#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
def show_sys_info():
    print(f"操作系统: {platform.system()} {platform.release()}")
    print(f"Python版本: {sys.version}")

def clear_screen():
    # 清除终端屏幕（适用于Windows和Unix/Linux）
    os.system('cls' if os.name == 'nt' else 'clear')

def show_history():
    print("最近使用的命令历史：")
    for cmd in command_history[-100:]:  # 只显示最后100个命令
        print(cmd)

def random_number(min_val, max_val):
    try:
        min_val = int(min_val)
        max_val = int(max_val)
        if min_val > max_val:
            print("错误：最小值不能大于最大值。")
            return
        print(random.randint(min_val, max_val))
    except ValueError:
        print("错误：最小值和最大值必须是整数。")

def add_numbers(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        print(f"{num1} + {num2} = {num1 + num2}")
    except ValueError:
        print("错误：提供的参数必须是整数。")
        #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
# 配置项
MEMO_DIRECTORY = "/storage/emulated/0/Adingtalksys/SoupOSv1.0.0/memoDTS0531"  # 示例路径，请根据实际情况修改
os.makedirs(MEMO_DIRECTORY, exist_ok=True)

MEMO_DATA = "/storage/emulated/0/Adingtalksys/SoupOSv1.0.0/data5431"  # 示例路径，请根据实际情况修改
os.makedirs(MEMO_DATA, exist_ok=True)

MEMO_NOTE = "/storage/emulated/0/Adingtalksys/SoupOSv1.0.0/note5418"  # 示例路径，请根据实际情况修改
os.makedirs(MEMO_NOTE, exist_ok=True)

# 确保MEMO_DIRECTORY是绝对路径，并且它存在
def create_memo(filename, content):
    """创建备忘录文件并写入内容"""
    filepath = os.path.join(MEMO_DIRECTORY, filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"备忘录已创建: {filepath}")
        return True
    except Exception as e:
        print(f"创建备忘录时发生错误: {e}")
        return False

def load_memo(filename):
    """加载备忘录内容"""
    filepath = os.path.join(MEMO_DIRECTORY, filename)

    if not os.path.isfile(filepath):
        print("该备忘录不存在.")
        return None
    #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            print("备忘录内容:")
            print(content)
            return content
    except Exception as e:
        print(f"读取备忘录时发生错误: {e}")
        return None

# 示例：如何调用这些函数（假设在Python环境中）
# 注意这里的调用方式使用了括号和引号
# create_memo('example.txt', '这是备忘录的内容')
# load_memo('example.txt')


# 日程管理

def add_schedule(username, name, time_str):
    """添加一个日程到用户的日程列表中"""
    schedules_path = os.path.join(MEMO_DATA, f"{username}_schedules.txt")
    
    try:
        schedule_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M')
        schedule_entry = f"事件名称: {name}, 时间: {schedule_time}\n"
        
        with open(schedules_path, 'a', encoding='utf-8') as file:
            file.write(schedule_entry)
        print(f"日程已添加到 {schedules_path}")
    except ValueError as ve:
        print(f"时间格式不正确: {ve}")
    except Exception as e:
        print(f"添加日程时发生错误: {e}")

def view_schedules(username):
    """查看所有日程"""
    schedules_path = os.path.join(MEMO_DATA, f"{username}_schedules.txt")
    #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
    try:
        if not os.path.exists(schedules_path):
            print("当前没有日程")
            return
        
        with open(schedules_path, 'r', encoding='utf-8') as file:
            print(file.read())
    except Exception as e:
        print(f"查看日程时发生错误: {e}")

def remove_schedule(username, index):
    """根据索引删除日程"""
    schedules_path = os.path.join(MEMO_DATA, f"{username}_schedules.txt")
    
    try:
        with open(schedules_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            if 0 <= index < len(lines):
                del lines[index]
                file.seek(0)
                file.truncate()
                file.writelines(lines)
                print(f"日程 {index} 已删除")
            else:
                print("索引超出范围")
    except Exception as e:
        print(f"删除日程时发生错误: {e}")

# 笔记管理

def create_note(username, title, content):
    """创建一条笔记并保存为TXT文件"""
    notes_directory = os.path.join(MEMO_NOTE, username)
    os.makedirs(notes_directory, exist_ok=True)
    
    note_filename = f"{title}.txt".replace(' ', '_')  # 确保文件名合法
    note_path = os.path.join(notes_directory, note_filename)
    
    try:
        with open(note_path, 'w', encoding='utf-8') as file:
            file.write(f"标题: {title}\n内容:\n{content}")
        print(f"笔记已创建: {note_path}")
    except Exception as e:
        print(f"创建笔记时发生错误: {e}")

def list_notes(username):
    """列出所有笔记"""
    notes_directory = os.path.join(MEMO_NOTE, username)
    #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
    try:
        if not os.path.exists(notes_directory) or not os.listdir(notes_directory):
            print("当前没有笔记")
            return
        
        notes_files = [f for f in os.listdir(notes_directory) if f.endswith('.txt')]
        for idx, note_file in enumerate(notes_files, start=1):
            print(f"{idx}. {note_file.replace('.txt', '').replace('_', ' ')}")
    except Exception as e:
        print(f"列出笔记时发生错误: {e}")

def show_note_content(username, index):
    """查看笔记内容"""
    notes_directory = os.path.join(MEMO_NOTE, username)
    
    try:
        notes_files = [f for f in os.listdir(notes_directory) if f.endswith('.txt')]
        if 0 <= index - 1 < len(notes_files):
            note_path = os.path.join(notes_directory, notes_files[index - 1])
            with open(note_path, 'r', encoding='utf-8') as file:
                print(file.read())
        else:
            print("索引超出范围")
    except Exception as e:
        print(f"查看笔记内容时发生错误: {e}")

def edit_note(username, index, new_title=None, new_content=None):
    """编辑笔记"""
    notes_directory = os.path.join(MEMO_NOTE, username)
    
    try:
        notes_files = [f for f in os.listdir(notes_directory) if f.endswith('.txt')]
        if 0 <= index - 1 < len(notes_files):
            note_path = os.path.join(notes_directory, notes_files[index - 1])
            
            with open(note_path, 'r+', encoding='utf-8') as file:
                lines = file.readlines()
                title_line = lines[0].strip().split(': ', 1)[1]
                content = ''.join(lines[2:])
                #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
                if new_title is not None:
                    title_line = new_title
                if new_content is not None:
                    content = new_content
                #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
                file.seek(0)
                file.truncate()
                file.write(f"标题: {title_line}\n内容:\n{content}")
            
            print(f"笔记 {index} 已更新")
        else:
            print("索引超出范围")
    except Exception as e:
        print(f"编辑笔记时发生错误: {e}")

def lucky():
    """生成并显示用户的幸运数字"""
    # 定义幸运数字的范围
    min_num = 1
    max_num = 100
    
    # 生成一个幸运数字
    lucky_number = random.randint(min_num, max_num)
    
    print(f"今日幸运数字: {lucky_number}")

def guess():
    """猜数字游戏"""
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("我已经想好了一个1到100之间的数字。你能猜出它是什么吗？")

    while True:
        try:
            guess = int(input("请输入你的猜测: "))
            attempts += 1
            if guess < number_to_guess:
                print("太小了！")
            elif guess > number_to_guess:
                print("太大了！")#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
            else:
                print(f"恭喜你！你猜对了！你总共猜了 {attempts} 次。")
                break
        except ValueError:
            print("请输入一个有效的数字。")

#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio

# 用于存储每日任务的字典
daily_tasks = defaultdict(list)

def add_task():
    """添加新任务"""
    task = input("请输入你要添加的任务: ")#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
    today = datetime.now().strftime('%Y-%m-%d')
    daily_tasks[today].append({'task': task, 'completed': False})#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
    print(f"任务 '{task}' 已添加到今天的任务列表中。")

def view_tasks():
    """查看今日任务"""
    today = datetime.now().strftime('%Y-%m-%d')
    if today in daily_tasks:#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        print("今日任务列表:")
        for idx, task_info in enumerate(daily_tasks[today], start=1):
            status = "已完成" if task_info['completed'] else "未完成"
            print(f"{idx}. [{status}] {task_info['task']}")
    else:
        print("今日没有任务。")

def generate_maze(width=10, height=10):
    if width % 2 == 0: width += 1
    if height % 2 == 0: height += 1
    
    maze = [['#' for _ in range(width)] for _ in range(height)]
    
    def carve(x, y):
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)
        #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                maze[y + dy // 2][x + dx // 2] = ' '
                maze[ny][nx] = ' '
                carve(nx, ny)
    
    maze[1][1] = 'S'
    carve(1, 1)
    maze[height-2][width-2] = 'E'
    #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))


#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # 初始饥饿值#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        self.happiness = 50  # 初始快乐值
        self.health = 100  # 初始健康值
        self.last_updated = time.time()


    def rename(self, new_name):
        """改名"""
        old_name = self.name#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        self.name = new_name
        print(f"{old_name} 的新名字是 {self.name}!")        

    def update_status(self):
        """根据时间更新宠物状态"""
        current_time = time.time()
        elapsed_time = (current_time - self.last_updated) / 60  # 转换为分钟
        self.hunger += elapsed_time * 2  # 每分钟饥饿值增加2点
        self.happiness -= elapsed_time * 1  # 每分钟快乐值减少1点#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        if self.hunger > 100: self.hunger = 100  # 最大值限制
        if self.happiness < 0: self.happiness = 0  # 最小值限制
        self.last_updated = current_time

    def feed(self):
        """喂食"""
        self.update_status()
        if self.hunger >= 20:#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
            self.hunger -= 20
            print(f"{self.name} 吃得很开心！")
        else:
            print(f"{self.name} 不太饿，不想吃东西。")

    def play(self):
        """玩耍"""
        self.update_status()
        if self.happiness <= 90:
            self.happiness += 10
            print(f"你和{self.name}玩得很开心！")
        else:
            print(f"{self.name} 已经很开心了！")

    def status(self):
        """显示宠物状态"""
        self.update_status()
        print(f"{self.name} 的状态:")
        print(f"饥饿值: {self.hunger}")
        print(f"快乐值: {self.happiness}")#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        print(f"健康值: {self.health}")

# 创建一只宠物实例
pet = Pet("Pooky")

def rename():
    new_name = input("请输入你想要给宠物的新名字: ").strip()
    if new_name:
        pet.rename(new_name)
    else:
        print("新名字不能为空，请重新尝试。")

def complete_task():
    """标记任务为已完成"""
    today = datetime.now().strftime('%Y-%m-%d')
    if today not in daily_tasks or not any(not task['completed'] for task in daily_tasks[today]):
        print("没有未完成的任务。")
        return
    #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
    view_tasks()
    try:
        task_index = int(input("请输入要标记为已完成的任务编号: ")) - 1
        if 0 <= task_index < len(daily_tasks[today]) and not daily_tasks[today][task_index]['completed']:
            daily_tasks[today][task_index]['completed'] = True
            print("任务已标记为已完成。")
        else:
            print("无效的任务编号或任务已经完成。")
    except (ValueError, IndexError):
        print("请输入有效的任务编号。")

def taskm():
    """任务管理主函数"""
    while True:
        print("\n任务管理菜单:")
        print("1. 添加新任务")
        print("2. 查看今日任务")
        print("3. 标记任务为已完成")
        print("4. 返回主菜单")
        
        choice = input("请选择操作 (1-4): ")
        #宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            break
        else:
            print("无效的选择，请重新选择。")

def feed():
    pet.feed()

def play():
    pet.play()

def status():
    pet.status()


def dai():
    """显示每日建议"""
    advices = [
        "尝试新事物可以拓展你的视野。",
        "不要害怕失败，它是成功的一部分。",
        "记得每天保持积极心态面对挑战。",
        "学习是一个持续的过程，每天都学一点新东西。",#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        "与家人和朋友保持联系，珍惜每一段关系。"
    ]
    
    # 从建议列表中随机选择一条建议
    advice_of_the_day = random.choice(advices)
    print(f"今日建议: {advice_of_the_day}")
#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio

def delete_note(username, index):
    """删除笔记"""
    notes_directory = os.path.join(MEMO_NOTE, username)
    
    try:
        notes_files = [f for f in os.listdir(notes_directory) if f.endswith('.txt')]
        if 0 <= index - 1 < len(notes_files):
            note_path = os.path.join(notes_directory, notes_files[index - 1])
            os.remove(note_path)
            print(f"笔记 {index} 已删除")#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
        else:
            print("索引超出范围")
    except Exception as e:
        print(f"删除笔记时发生错误: {e}")
# 统一的命令表及描述
commands = {
    'time': (show_time, "显示当前时间"),
    'help': (help_command, "显示所有命令"),
    'private': (private_space, "进入隐私空间"),
    'exit': (lambda: (print("感谢使用，再见！"), exit()), "退出程序"),
    'exit-2': (lambda username: (print("您已成功退出登录."), main()), "退出登录"),
    'sysinfo': (show_sys_info, "显示系统信息"),
    'clear': (clear_screen, "清除屏幕"),
    'random-number': (random_number, "生成指定范围内的随机整数"),#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
    'add': (add_numbers, "计算两个数字之和"),
    'history': (show_history, "查看命令历史"),
    'dtsys': (dtsys, " "),
    'errorno': (errorno, "收集错误信息并发送给宜鸽工作室信息分析平台"),
    'create_memo': (create_memo, "创建一个新的备忘录，格式为: create_memo 文件名 内容"),
    'load_memo': (load_memo, "加载现有的备忘录，格式为: load_memo 文件名"),
    'add_schedule': (lambda u, n, t: add_schedule(u, n, t), "添加一个日程，格式为: add_schedule '事件名称' 'YYYY-MM-DD HH:MM'"),
    'view_schedules': (lambda u: view_schedules(u), "查看所有日程"),
    'remove_schedule': (lambda u, i: remove_schedule(u, int(i)), "根据索引删除日程，格式为: remove_schedule 索引"),
    'create_note': (lambda u, t, c: create_note(u, t, c), "创建一条笔记，格式为: create_note '标题' '内容'"),
    'list_notes': (lambda u: list_notes(u), "列出所有笔记"),
    'show_note': (lambda u, i: show_note_content(u, int(i)), "查看笔记内容，格式为: show_note 索引"),
    'edit_note': (lambda u, i, t=None, c=None: edit_note(u, int(i), t, c), "编辑笔记，格式为: edit_note 索引 [新标题] [新内容]"),
    'delete_note': (lambda u, i: delete_note(u, int(i)), "删除笔记，格式为: delete_note 索引"),
    'generate_password': (generate_password, "生成随机密码"),
    'dai':(dai, "显示每日建议"),
    'lucky':(lucky, "幸运数字"),#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
    'guess':(guess, "猜数字"),
    'feed': (feed, "喂你的虚拟宠物"),
    'play': (play, "和你的虚拟宠物玩耍"),
    'status': (status, "查看你的虚拟宠物的状态"),
    'rename': (rename, "给你的虚拟宠物改名"),
    'taskm': (taskm, "管理你的每日任务")
}
def load_user_data():
    """加载用户的个人数据结构"""
    global schedules, notes, note_id_counter
    
    # 初始化日程和笔记为空字典，默认情况下不从文件加载
    schedules = defaultdict(list)
    notes = defaultdict(list)
    note_id_counter = 0
    
    return schedules, notes, note_id_counter
#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
def parse_command(command_input, username):
    parts = command_input.split(' ', 2)  # 将输入分为命
    command = parts[0]
    args = parts[1:] if len(parts) > 1 else []#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio

    if command in commands:
        func, desc = commands[command]
        try:
            if command == 'generate_password':
                func()  # 不需要用户名参数
            elif command == 'private' or command == 'exit-2':
                func(username)
            elif command == 'random-number':
                if len(args) < 2:
                    print("错误：'random-number'命令需要最小值和最大值作为参数。")
                    return
                func(args[0], args[1])
            elif command == 'add':
                if len(args) < 2:
                    print("错误：'add'命令需要两个数字作为参数。")
                    return
                func(args[0], args[1])
            elif command in ['create_memo', 'load_memo']:
                if command == 'create_memo':
                    if len(parts) < 3:
                        print("需要提供文件名和备忘录内容")
                        return
                    func(parts[1], ' '.join(parts[2:]))
                elif command == 'load_memo':
                    if len(parts) < 2:
                        print("需要提供备忘录文件名")
                        return
                    func(parts[1])
            elif command in ['add_schedule', 'remove_schedule', 'show_note', 'edit_note', 'delete_note']:
                if len(parts) < 3:
                    print("命令格式不正确，请参考帮助信息。")#宜鸽工作室赵丛瑞   15163473881     钉钉号yigestudio
                    return
                func(username, *parts[1:])
            else:
                func(username, *args)

            command_history.append(command_input)  # 添加到命令历史中
        except Exception as e:
            print(f"执行命令时发生错误: {e}")
    else:
        print(f"未知命令: '{command}'。请输入 'help' 查看所有命令。")


def main():
    print("欢迎来到SoupOSv1.0.0，请先登录")

    while True:
        username = input("用户名：").strip()
        password = getpass.getpass("密码：").strip()  # 使用getpass隐藏密码输入

        if accounts.get(username) == password:
            print(f"欢迎进入本系统，{username}")
            print(f"   提示：输入help查看指令。")
            break
        else:
            print("账号或密码错误，请重试")


    while True:
        command_input = input(f"{username}>>> ").strip().lower()
        command_history.append(command_input)  # 添加到命令历史中
        
        parts = command_input.split(' ', 2)  # 将输入分为命令、成员名和参数
        
        command = parts[0]
        arg1 = None
        arg2 = None

        if len(parts) > 1:
            arg1 = parts[1].strip("'\"") if len(parts) > 1 else None
            if len(parts) > 2:
                arg2 = parts[2]

        if command in commands:
            func, _ = commands[command]
            try:
                if command in ['private', 'exit-2']:
                    func(username)
                elif command == 'random-number':
                    if arg1 is None or arg2 is None:
                        print("错误：'random-number'命令需要最小值和最大值作为参数。")
                        continue
                    func(arg1, arg2)
                elif command == 'add':
                    if arg1 is None or arg2 is None:
                        print("错误：'add'命令需要两个数字作为参数。")
                        continue
                    func(arg1, arg2)
                elif command in ['create_memo', 'load_memo']:
                    if command == 'create_memo':
                       if len(parts) < 3:
                        print("需要提供文件名和备忘录内容")
                        continue
                    func(parts[1], ' '.join(parts[2:]))

                elif command == 'load_memo':
                    if len(parts) < 2:
                        print("需要提供备忘录文件名")
                        continue
                    func(parts[1])

                elif command == 'exit':
                    func()
                    return
                else:
                    func()
            except Exception as e:
                print(f"执行命令时发生错误: {e}")
        else:
            print("未知命令，请输入'help'查看所有命令")

if __name__ == "__main__":
    main()









"""
本次更新:去除钉钉api
猜数字
幸运数字
建议盲盒
电子宠物

每日任务
"""