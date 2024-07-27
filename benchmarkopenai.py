from openai import OpenAI
import time

# Replace 'your-api-key-here' with your actual OpenAI API key
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

print('Sleeping for 500s')
time.sleep(500)
print('Sleep Ended')

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_api_key,
    base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id

def chat_with_gpt(prompt):
    try:
        start_time = time.time()
        # Make a request to the OpenAI API
        response = client.completions.create(
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            model=model        )
        
        # Extract and return the response text
        print("--- %s seconds ---" % (time.time() - start_time))
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

text = '''
July 28, 2024 – New York — Wall Street saw a significant rally today, with major indices posting solid gains following a slew of stronger-than-expected earnings reports and positive economic data.

The S&P 500 jumped 1.2%, the Dow Jones Industrial Average climbed 0.9%, and the Nasdaq Composite soared 1.5%, reflecting widespread investor enthusiasm. The rally was driven by impressive quarterly results from leading companies and encouraging signs from the economy.

Key Earnings Reports

Tech giants led the charge, with Apple Inc. and Microsoft Corp. both exceeding profit forecasts. Apples robust sales of its latest iPhone and Microsofts strong performance in its cloud division fueled optimism. In the retail sector, Amazon.com Inc. also delivered strong results, with better-than-expected earnings bolstered by successful promotional events and market expansion.

Economic Data Boost

Today's positive market sentiment was further supported by economic data. The U.S. Commerce Department reported a 3.2% annualized growth rate for the second quarter, surpassing expectations and highlighting the strength of consumer spending and business investment. Additionally, the Labor Departments report showed a decrease in initial jobless claims, signaling a resilient labor market.

Market Outlook

Analysts are optimistic about the market's direction. “Todays earnings and economic data paint a positive picture for the second half of the year,” said Jane Roberts, senior analyst at Capital Insights. “While there are still risks, such as geopolitical tensions and inflation concerns, the current data suggests the economy remains robust.”

Sector Highlights

Technology stocks were the standout performers, with gains across the semiconductor and software sectors. The energy sector also benefited from rising oil prices, although the healthcare sector lagged due to regulatory challenges.

As earnings season progresses, investors will be watching closely for results from major firms like Tesla and Alphabet Inc., as well as upcoming economic reports for further guidance on market trends.

Conclusion

Todays market gains reflect a mix of strong corporate earnings and favorable economic indicators, offering a hopeful outlook for the remainder of the year. However, investors remain vigilant for any potential disruptions that could affect market stability.
'''

prompt = (
            "Write a youtube video script using below article\n\n"
            f"{text}\n\n"
        )


response = chat_with_gpt(prompt)

print('RESPONSE STARTED HERE')
print(response)
print('RESPONSE ENDED HERE')
