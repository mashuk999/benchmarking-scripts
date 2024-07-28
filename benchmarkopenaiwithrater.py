from openai import OpenAI
import time
import socket

time.sleep(300)

# Replace 'your-api-key-here' with your actual OpenAI API key
openai_api_key_chat = "EMPTY"
openai_api_base_chat = "http://localhost:8000/v1"

openai_api_key_rater = "EMPTY"
openai_api_base_rater = "http://localhost:8080/v1"

chat_client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY_chat")
    api_key=openai_api_key_chat,
    base_url=openai_api_base_chat,
)
models_chat = chat_client.models.list()
model_chat = models_chat.data[0].id

rater_client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY_chat")
    api_key=openai_api_key_rater,
    base_url=openai_api_base_rater,
)
models_rater = rater_client.models.list()
model_rater = models_rater.data[0].id

def chat_with_gpt(prompt):
    try:
        start_time = time.time()
        # Make a request to the OpenAI API
        response = chat_client.completions.create(
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7,
            model=model_chat        )
        
        # Extract and return the response text
        print("--- %s seconds ---" % (time.time() - start_time))
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def chat_with_rater(prompt):
    try:
        start_time = time.time()
        # Make a request to the OpenAI API
        response = rater_client.completions.create(
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7,
            model=model_rater        )
        
        # Extract and return the response text
        print("--- %s seconds ---" % (time.time() - start_time))
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

text = '''
**Bollywood Buzz: Exciting Developments and Upcoming Releases**

Bollywood continues to captivate audiences worldwide with its blend of drama, music, and star power. Recent weeks have been particularly eventful, with several exciting developments making headlines.

**1. New Film Announcements:**

The much-anticipated collaboration between celebrated director Rajkumar Hirani and superstar Shah Rukh Khan has been officially confirmed. The film, tentatively titled *Dard-e-Dil*, is expected to be a heartfelt drama with Hirani's signature blend of humor and emotion. Fans are eagerly awaiting more details on the plot and the rest of the cast.

**2. Star Weddings and Celebrations:**

The Bollywood social scene has been abuzz with the news of Alia Bhatt and Ranbir Kapoor's recent anniversary celebration. The couple, who are also new parents, hosted an intimate gathering with close friends and family, sharing glimpses of their joy on social media. Their daughter, Raha, has already become a favorite among fans, with her adorable photos making frequent appearances online.

**3. Upcoming Releases:**

Several high-profile films are set to hit theaters in the coming months. *Dilwale* director Rohit Shetty's latest action-packed venture, *Aag*, promises to deliver explosive entertainment. Starring Ajay Devgn and Kriti Sanon, the film is generating buzz for its grand scale and impressive stunts.

Additionally, *Jab We Met* director Imtiaz Ali is gearing up for the release of his new romantic drama, *Chandni Raatein*. With a stellar cast including Kartik Aaryan and Janhvi Kapoor, the film is expected to be a visual and emotional treat.

**4. Awards and Recognitions:**

Bollywood's award season is in full swing, and this year's nominations have sparked much discussion. *Pathaan*, starring Shah Rukh Khan and Deepika Padukone, has garnered critical acclaim and is leading the race for several major awards. Meanwhile, rising star Ayushmann Khurrana is being praised for his compelling performance in *Meri Zindagi*, which has positioned him as one of the most versatile actors of his generation.

**5. Industry Insights:**

As Bollywood evolves, so does its approach to storytelling and production. The rise of digital platforms has led to a surge in web series and online content, with many established actors and directors exploring this new medium. This shift is not only expanding the scope of Bollywood narratives but also providing audiences with fresh and diverse content.

As always, Bollywood remains a dynamic and vibrant industry, with new stories, stars, and surprises around every corner. Stay tuned for more updates as the drama and excitement continue to unfold in India's film capital.
'''

prompt = (
            "Write a youtube script using below article\n\n"
            f"{text}\n\n"
        )


response = chat_with_gpt(prompt)

print('RESPONSE STARTED HERE')
print(response)
print('RESPONSE ENDED HERE')

prompt = (
            "Rate the below article frim 0 to 10. Do not provide any text just one word answer\n\n"
            f"{response}\n\n"
        )
response = chat_with_rater(prompt)
print('=======')
print('RESPONSE STARTED HERE')
print(response)
print('RESPONSE ENDED HERE')
