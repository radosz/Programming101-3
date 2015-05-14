import os


TimeExceptionMessages = "Please enter correct time !"


class TimeException(Exception):

    def __str__(self):
        return TimeExceptionMessages


class Cron:

    @staticmethod
    def start_every_day_at(hour, minute, file_name):
        Cron.__create_task_file(file_name)
        cmd_start = "./start_at"

        minute = int(minute)
        hour = int(hour)

        if minute > 60 or hour > 24:
            raise TimeException

        if minute <= 9:
            minute = "0" + str(minute)

        if hour <= 9:
            hour = "0" + str(hour)

        w_dir = os.getcwd()

        task = "{} {} * * * env DISPLAY=:0 {}/task.sh".format(
            minute, hour, w_dir, os.getcwd())
        with open("start_at.crontab", "w") as start:
            start.write(task)
            start.close()
        os.system(cmd_start)

    @staticmethod
    def __create_task_file(command):
        file_str = """
#!/bin/sh
#!/bin/python3.4
cd "{}"
python3 "{}"
""".format(os.getcwd(), command)
        command = "chmod +x task.sh"
        with open("task.sh", "w") as start:
            start.write(file_str)
            start.close()
        os.system(command)


def main():
    Cron.start_every_day_at(hour="12", minute="30", file_name="server.py")

if __name__ == '__main__':
    main()
