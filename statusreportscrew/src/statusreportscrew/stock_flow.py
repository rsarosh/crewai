from crewai.flow.flow import Flow, listen, start, and_, or_
from dotenv import load_dotenv
from litellm import completion
import os
import requests
from bs4 import BeautifulSoup
from statusreportscrew.utils import get_latest_stock_news_via_api
from pydantic import BaseModel

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

class StockState (BaseModel):
    news : str = ""


class StockFlow(Flow [StockState]):
    model = "gpt-4o"

    @start()
    def get_stock_data(self):
        print("Starting flow")
        # Each flow state automatically gets a unique ID
        # print(f"Flow State ID: {self.state['id']}")
        with open(os.path.join(os.path.dirname(__file__),  "rpt.txt"), "r") as file:
            content = file.read()
            return content

    @listen(get_stock_data)
    def get_stock_news(self, stock_data):
        stock_name = stock_data.split("Stock: ")[1].split("\n")[0]
        _news = ""
        headlines = get_latest_stock_news_via_api(stock_name)
        for idx, news in enumerate(headlines, start=1):
            _news += news["title"] + "\n\n"
        self.state.news = _news
        stock_data += "\n\nNews: " + _news
        print (f"Stock Data: {stock_data}")
        return stock_data

    #and conditons
    @listen(and_(get_stock_data,get_stock_news))
    def get_stock_report(self, stock_data):
        prompt = f"Analyze the following stock report and provide insights with clear recommendation on top of buy, sell or hold. Don't remove the News headlines, print the full company name on top with the recommendation: {stock_data}"
        messages = [
            {
                "system": "You are a Financial Analyst, who knows everythign about stocks. You keep up with current news and trends, and you have a deep understanding of stock market dynamics.",
                "role": "user",
                "content": prompt,
            }
        ]

        response = completion(
            model=self.model,
            api_key=OPENAI_API_KEY,
            messages=messages,
        )
        stock_report = response["choices"][0]["message"]["content"]
        stock_report += "\n\nNews: " + self.state.news
        with open("stock_report.md", "w") as file:
            file.write(stock_report)
      
        print(f"Done creating Stock Report")
        return stock_report

