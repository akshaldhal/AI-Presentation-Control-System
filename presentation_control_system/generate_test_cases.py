from .test_generator import TestGenerator
import csv

def generate_test_cases(num_presentations: int = 10):
    generator = TestGenerator()
    with open('tests/presentation_tests.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["business_idea", "business_name", "slides", "narrator", "index"])

        for i in range(num_presentations):
            try:
                business_idea = generator.generate_business_idea()
                business_name = generator.generate_business_name(business_idea)
                slides = generator.generate_presentation(business_idea)

                for idx, slide in enumerate(slides):
                    narration = generator.generate_narration(slide)
                    writer.writerow([business_idea, business_name, slide, narration, idx + 1])

                if (i + 1) % 10 == 0:
                    print(f"Generated {i + 1} presentations")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    generate_test_cases(num_presentations=10)
