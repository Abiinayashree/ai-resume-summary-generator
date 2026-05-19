from groq import Groq

client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)

while True:

    user_input = input("Enter your skills and experience: ")

    if user_input.lower() == "exit":
        print("Program Ended.")
        break

    prompt = f"Generate a professional resume summary for: {user_input}"

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.1-8b-instant"
    )

    print("\nProfessional Summary:\n")
    print(response.choices[0].message.content)