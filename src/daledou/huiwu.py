from src.daledou.daledou import DaLeDou


class HuiWu(DaLeDou):
    '''会武'''

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get(params: str):
        global html
        html = DaLeDou.get(params)

    def 挑战(self):
        for _ in range(21):
            # 挑战
            HuiWu.get('cmd=sectmelee&op=dotraining')
            self.msg.append(DaLeDou.search(r'最高伤害：\d+<br />(.*?)<br />'))
            if '你已达今日挑战上限' in html:
                self.msg.append(DaLeDou.search(r'规则</a><br />(.*?)<br />'))
                break
            elif '你的试炼书不足' in html:
                # 兑换 试炼书*10
                HuiWu.get(
                    'cmd=exchange&subtype=2&type=1265&times=10&costtype=13')

    def 助威(self):
        # 冠军助威 丐帮
        HuiWu.get('cmd=sectmelee&op=cheer&sect=1003')
        # 冠军助威
        HuiWu.get('cmd=sectmelee&op=showcheer')
        self.msg.append(DaLeDou.search(r'【冠军助威】<br />(.*?)<br /><br />'))

    def 领奖(self):
        # 领奖
        HuiWu.get('cmd=sectmelee&op=drawreward')
        self.msg.append(DaLeDou.search(r'【领奖】<br />(.*?)<br />.*?领取'))

    def 兑换(self):
        # 兑换 真黄金卷轴*10
        HuiWu.get('cmd=exchange&subtype=2&type=1263&times=10&costtype=13')
        self.msg.append(DaLeDou.search(r'】<br />(.*?)<br />'))

    def run(self) -> list:
        if self.week in ['1', '2', '3']:
            self.挑战()
        elif self.week == '4':
            self.助威()
        elif self.week == '6':
            self.领奖()
            self.兑换()

        return self.msg
