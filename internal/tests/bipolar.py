from models.schemas import Test, TestScore, TestQuestion

options = {"YES": 1, "NO": 0}

bipolar_test = Test(
    name="Bipolar Test",
    prompt="Please answer each question to the best of your ability.\
        \nPlease note, all fields are required.",
    scores=[
        TestScore(score=(0, 2), result="Minimal Bipolar"),
        TestScore(score=(3, 7), result="Mild Bipolar"),
        TestScore(score=(8, 13), result="Moderate Bipolar"),
        TestScore(score=(14, 19), result="Severe Bipolar"),
    ],
    content={
        1: TestQuestion(
            question="Has there ever been a period of time when you were not your usual self and...you felt so good or so hyper that other people thought you were not your normal self or you were so hyper that you got into trouble?",
            options=options,
        ),
        2: TestQuestion(
            question="...you were so irritable that you shouted at people or started fights or arguments?",
            options=options,
        ),
        3: TestQuestion(
            question="...you felt much more self-confident than usual?",
            options=options,
        ),
        4: TestQuestion(
            question="...you got much less sleep than usual and found you didn’t really miss it?",
            options=options,
        ),
        5: TestQuestion(
            question="...you were much more talkative or spoke much faster than usual?",
            options=options,
        ),
        6: TestQuestion(
            question="...thoughts raced through your head or you couldn’t slow your mind down?",
            options=options,
        ),
        7: TestQuestion(
            question="...you were so easily distracted by things around you that you had trouble concentrating or staying on track?",
            options=options,
        ),
        8: TestQuestion(
            question="...you had much more energy than usual?",
            options=options,
        ),
        9: TestQuestion(
            question="...you were much more active or did many more things than usual?",
            options=options,
        ),
        10: TestQuestion(
            question="...you were much more social or outgoing than usual, for example, you telephoned friends in the middle of the night?",
            options=options,
        ),
        11: TestQuestion(
            question="...you were much more interested in sex than usual?",
            options=options,
        ),
        12: TestQuestion(
            question="...you did things that were unusual for you or that other people might have thought were excessive, foolish, or risky?",
            options=options,
        ),
        13: TestQuestion(
            question="...spending money got you or your family into trouble?",
            options=options,
        ),
        14: TestQuestion(
            question="If you checked YES to more than one of the above, have several of these ever happened during the same period of time?",
            options=options,
        ),
        15: TestQuestion(
            question="How much of a problem did any of these cause you - like being unable to work; having family, money or legal troubles; getting into arguments or fights?",
            options={
                "NO PROBLEM": 0,
                "MINOR PROBLEM": 1,
                "MODERATE PROBLEM": 2,
                "SERIOUS PROBLEM": 3,
            },
        ),
        16: TestQuestion(
            question="Have any of your blood relatives (i.e. children, siblings, parents, grandparents, grandchildren, aunts, uncles) had manic-depressive illness or bipolar disorder?",
            options=options,
        ),
        17: TestQuestion(
            question="Has a health professional ever told you that you have manic-depressive illness or bipolar disorder?",
            options=options,
        ),
    },
)
