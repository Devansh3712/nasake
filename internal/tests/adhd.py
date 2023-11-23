from models.schemas import Test, TestScore, TestQuestion

options: dict[str, int] = {
    "NEVER": 0,
    "RARELY": 1,
    "SOMETIMES": 2,
    "OFTEN": 3,
    "VERY OFTEN": 4,
}

adhd_test = Test(
    name="ADHD Test",
    prompt="Please answer the questions below, rating yourself on each of the criteria shown. \
        As you answer each question, select the button that best describes how you have felt and conducted yourself over the past 6 months.",
    scores=[
        TestScore(score=(0, 17), result="No Signs of ADHD"),
        TestScore(score=(18, 35), result="Mild Signs of ADHD"),
        TestScore(score=(36, 54), result="Moderate Signs of ADHD"),
        TestScore(score=(55, 72), result="Severe Signs of ADHD"),
    ],
    content={
        1: TestQuestion(
            question="How often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?",
            options=options,
        ),
        2: TestQuestion(
            question="How often do you have difficulty getting things in order when you have to do a task that requires organization?",
            options=options,
        ),
        3: TestQuestion(
            question="How often do you have problems remembering appointments or obligations?",
            options=options,
        ),
        4: TestQuestion(
            question="When you have a task that requires a lot of thought, how often do you avoid or delay getting started?",
            options=options,
        ),
        5: TestQuestion(
            question="How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?",
            options=options,
        ),
        6: TestQuestion(
            question="How often do you feel overly active and compelled to do things, like you were driven by a motor?",
            options=options,
        ),
        7: TestQuestion(
            question="How often do you make careless mistakes when you have to work on a boring or difficult project?",
            options=options,
        ),
        8: TestQuestion(
            question="How often do you have difficulty keeping your attention when you are doing boring or repetitive work?",
            options=options,
        ),
        9: TestQuestion(
            question="How often do you have difficulty concentrating on what people say to you, even when they are speaking to you directly?",
            options=options,
        ),
        10: TestQuestion(
            question="How often do you misplace or have difficulty finding things at home or at work?",
            options=options,
        ),
        11: TestQuestion(
            question="How often are you distracted by activity or noise around you?",
            options=options,
        ),
        12: TestQuestion(
            question="How often do you leave your seat in meetings or other situations in which you are expected to remain seated?",
            options=options,
        ),
        13: TestQuestion(
            question="How often do you feel restless or fidgety?",
            options=options,
        ),
        14: TestQuestion(
            question="How often do you have difficulty unwinding and relaxing when you have time to yourself?",
            options=options,
        ),
        15: TestQuestion(
            question="How often do you find yourself talking too much when you are in social situations?",
            options=options,
        ),
        16: TestQuestion(
            question="When you're in a conversation, how often do you find yourself finishing the sentences of the people you are talking to before they can finish them themselves?",
            options=options,
        ),
        17: TestQuestion(
            question="How often do you have difficulty waiting your turn in situations when turn taking is required?",
            options=options,
        ),
        18: TestQuestion(
            question="How often do you interrupt others when they are busy?",
            options=options,
        ),
    },
)
