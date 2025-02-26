import json
import time
import os
import random
import google.generativeai as genai

# Configure Gemini API with your key
genai.configure(api_key='AIzaSyC_OCnmU3eQUn0IhDUyY6nyMdcI0hM8Vik')

# Subjects for question generation
subjects = ["Indian History", "Geography", "Polity"]


# Generate questions with Gemini
def generate_question_with_gemini(subject):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = (
        f"Generate a multiple-choice question (MCQ) for {subject} related to competitive exams in India (e.g., UPSC, SSC). "
        f"Provide:\n"
        f"1. The question\n"
        f"2. Four options labeled A), B), C), D)\n"
        f"3. The correct answer as a single letter (A, B, C, or D)\n"
        f"Format the response as:\n"
        f"Question: [Your question]\n"
        f"A) [Option 1]\n"
        f"B) [Option 2]\n"
        f"C) [Option 3]\n"
        f"D) [Option 4]\n"
        f"Answer: [A/B/C/D]"
    )
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        print(f"Gemini generated:\n{text}\n")  # Debug output

        # Parse the response with flexibility
        lines = [line.strip() for line in text.split('\n') if line.strip()]  # Remove empty lines
        if len(lines) < 6:
            raise ValueError(f"Incomplete response: {lines}")

        # Extract question (assume it starts with "Question:")
        question_line = next((line for line in lines if line.startswith("Question:")), None)
        if not question_line:
            raise ValueError("No question found")
        question = question_line.replace("Question: ", "").strip()

        # Extract options (lines starting with A), B), C), D))
        options = []
        for line in lines:
            for prefix in ["A)", "B)", "C)", "D)"]:
                if line.startswith(prefix):
                    options.append(line.strip())
        if len(options) != 4:
            raise ValueError(f"Expected 4 options, got: {options}")

        # Extract answer (line starting with "Answer:")
        answer_line = next((line for line in lines if line.startswith("Answer:")), None)
        if not answer_line:
            raise ValueError("No answer found")
        answer = answer_line.replace("Answer: ", "").strip().upper()  # Normalize to uppercase

        # Validate answer
        if answer not in ['A', 'B', 'C', 'D']:
            raise ValueError(f"Invalid answer format: '{answer}'")

        return {
            "question": question,
            "options": options,
            "answer": answer
        }
    except Exception as e:
        print(f"Gemini Generation Error: {e}")
        return None


# Main function
def generate_and_save_questions(target_questions=10, questions_per_file=5):
    start_time = time.time()
    folder_name = "questions_folder"
    os.makedirs(folder_name, exist_ok=True)

    questions_list = []
    file_number = 1

    for i in range(target_questions):
        subject = random.choice(subjects)
        question_data = generate_question_with_gemini(subject)

        if question_data:
            questions_list.append(question_data)
            print(f"Generated: {question_data['question']}")
        else:
            print(f"Failed to generate question for {subject}")

        if len(questions_list) >= questions_per_file:
            file_path = os.path.join(folder_name, f"questions_batch_{file_number}.json")
            with open(file_path, "w") as f:
                json.dump(questions_list, f, indent=4)
            print(f"Saved {len(questions_list)} questions to {file_path}")
            questions_list = []
            file_number += 1

    if questions_list:
        file_path = os.path.join(folder_name, f"questions_batch_{file_number}.json")
        with open(file_path, "w") as f:
            json.dump(questions_list, f, indent=4)
        print(f"Saved remaining {len(questions_list)} questions to {file_path}")

    print(f"Total time: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    generate_and_save_questions()