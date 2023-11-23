from models.schemas import Test, TestQuestion, TestScore

options = {"NEVER": 0, "SOMETIMES": 1, "OFTEN": 2}

youth_test = Test(
    name="Youth Test",
    prompt="Pediatric Symptom Checklist - Youth Report\nThe questionnaire that follows can be used to see if you are having emotional, attentional, or behavioral difficulties. \
        For each item please mark how often you:",
    scores=[
        TestScore(
            score=(0, 15),
            result="No Signs of Emotional, Attentional, or Behavioral Difficulties",
        ),
        TestScore(
            score=(16, 31),
            result="Mild Signs of Emotional, Attentional, or Behavioral Difficulties",
        ),
        TestScore(
            score=(32, 45),
            result="Moderate Signs of Emotional, Attentional, or Behavioral Difficulties",
        ),
        TestScore(
            score=(46, 70),
            result="Severe Signs of Emotional, Attentional, or Behavioral Difficulties",
        ),
    ],
    content={
        1: TestQuestion(
            question="Complain of aches or pains",
            options=options,
        ),
        2: TestQuestion(
            question="Spend more time alone",
            options=options,
        ),
        3: TestQuestion(
            question="Tire easily, have little energy",
            options=options,
        ),
        4: TestQuestion(
            question="Fidgety, unable to sit still",
            options=options,
        ),
        5: TestQuestion(
            question="Have trouble with teacher(s)",
            options=options,
        ),
        6: TestQuestion(
            question="Less interested in school",
            options=options,
        ),
        7: TestQuestion(
            question="Act as if driven by motor",
            options=options,
        ),
        8: TestQuestion(
            question="Daydream too much",
            options=options,
        ),
        9: TestQuestion(
            question="Distract easily",
            options=options,
        ),
        10: TestQuestion(
            question="Are afraid of new situations",
            options=options,
        ),
        11: TestQuestion(
            question="Feel sad, unhappy",
            options=options,
        ),
        12: TestQuestion(
            question="Are irritable, angry",
            options=options,
        ),
        13: TestQuestion(
            question="Feel hopeless",
            options=options,
        ),
        14: TestQuestion(
            question="Have trouble concentrating",
            options=options,
        ),
        15: TestQuestion(
            question="Less interested in friends",
            options=options,
        ),
        16: TestQuestion(
            question="Fight with other children",
            options=options,
        ),
        17: TestQuestion(
            question="Absent from school",
            options=options,
        ),
        18: TestQuestion(
            question="School grades dropping",
            options=options,
        ),
        19: TestQuestion(
            question="Down on yourself",
            options=options,
        ),
        20: TestQuestion(
            question="Visit doctor with doctor finding nothing wrong",
            options=options,
        ),
        21: TestQuestion(
            question="Have trouble sleeping",
            options=options,
        ),
        22: TestQuestion(
            question="Worry a lot",
            options=options,
        ),
        23: TestQuestion(
            question="Want to be with parent more than before",
            options=options,
        ),
        24: TestQuestion(
            question="Feel that you are bad",
            options=options,
        ),
        25: TestQuestion(
            question="Take unnecessary risks",
            options=options,
        ),
        26: TestQuestion(
            question="Get hurt frequently",
            options=options,
        ),
        27: TestQuestion(
            question="Seem to be having less fun",
            options=options,
        ),
        28: TestQuestion(
            question="Act younger than children your age",
            options=options,
        ),
        29: TestQuestion(
            question="Do not listen to rules",
            options=options,
        ),
        30: TestQuestion(
            question="Do not show feelings",
            options=options,
        ),
        31: TestQuestion(
            question="Do not understand other people's feelings",
            options=options,
        ),
        32: TestQuestion(
            question="Tease others",
            options=options,
        ),
        33: TestQuestion(
            question="Blame others for your troubles",
            options=options,
        ),
        34: TestQuestion(
            question="Take things that do not belong to you",
            options=options,
        ),
        35: TestQuestion(
            question="Refuse to share",
            options=options,
        ),
        36: TestQuestion(
            question="Do you have any emotional or behavioral problems for which you need help?",
            options={"YES": 0, "NO": 1},
        ),
    },
)
