import json
import time
from rich import print
from rich.console import Console

class Data:

    def __init__(self):
        pass
    
    @classmethod
    def printColoredText(self, text, color, total):
        console = Console()
        delay = total / len(text)
        for char in text:
            if char == '.':
                console.print(char, style='bold magenta', end="")
            else:
                console.print(char, style=color, end="")
            time.sleep(delay)
        console.print()

    @classmethod
    def algorithm(self):
        filename = 'output.json'
        with open(filename, 'r') as file:
            data = json.load(file)
            dic = {}
            deals = []
            for d in data:
                priceUSD = round(float(d['price (yuan)']) * 0.1429, 4)
                priceYUAN = round(float(d['price (yuan)']), 4)
                balanceSorpack = float(d['balance ($)'])
                cardNumber = d['card number']
                serialNumber = d['serial number']
                ratio = round(balanceSorpack / priceUSD, 3)
                deals.append([ratio, balanceSorpack, priceUSD, cardNumber, serialNumber, priceYUAN])
            
            deals = sorted(deals, reverse=True, key=lambda x: x[0])
            print('[bold green]' + "------------------------------" + '[/bold green]' + '[bold white]' + " Top 10 Deals [bold white]([/bold white][bold green]Best[/bold green] to [bold red]Worst[/bold red][bold white])[/bold white] " + '[/bold white]' + '[bold green]' + "------------------------------" + '[/bold green]')
            print('[bold white]http://sorpack.com/new_plus/shop/shop_card.asp[/bold white]')
            print('[bold green]' + "------------------------------------------------------------------------------------------" + '[/bold green]')
            time.sleep(0.5)
            for i in range(10):
                deal = deals[i]
                ratio = format(int(deal[0]), ',')
                balance = format(int(deal[1]), ',')
                priceUSD = round(deal[2], 2)
                cardNumber = deal[3]
                serialNumber = deal[4]
                priceYUAN = int(deal[5])
            
                if i == 0:
                    self.printColoredText("The Best Deal Right Now is...", 'bold yellow', 1)
                    self.printColoredText(f"{serialNumber}) {cardNumber} ${balance} for {priceYUAN} yuan. With a ratio of ${ratio} per dollar.", 'white', 1.5)
                    time.sleep(0.2)
                    print('[bold green]' + "------------------------------------------------------------------------------------------" + '[/bold green]')
                    time.sleep(1)
                    continue
                self.printColoredText(f"{serialNumber}) {cardNumber} ${balance} for {priceYUAN} yuan. With a ratio of ${ratio} per dollar.", 'white', 0.3)
                print()
                time.sleep(0.1)
        