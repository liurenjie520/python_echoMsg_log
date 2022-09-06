import sys

class msg():
    def echoMsg(self, level, msg):
        if level == 'Info':
            print('[Info] %s' % msg)

        elif level == 'Error':
            print('[Error] %s' % msg)

   

    def log(self):
        self.echoMsg('Info', '新闻数目获取成功')
        self.echoMsg('Error', '新闻数目获取Error')
        try:
            a=1
            b="2"
            c=a+b
            print(c)
        except Exception as e:
            # 异常错误
            self.echoMsg('Error', e)
            sys.exit()


if __name__ == '__main__':
    p=msg()
    p.log()
    # [Info] 新闻数目获取成功
    # [Error] 新闻数目获取Error
    # [Error] unsupported operand type(s) for +: 'int' and 'str'

