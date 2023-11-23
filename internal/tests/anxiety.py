from models.schemas import Test, TestScore, TestQuestion

options: dict[str, int] = {
    "NOT AT ALL": 0,
    "SEVERAL DAYS": 1,
    "MORE THAN HALF THE DAYS": 2,
    "NEARLY EVERY DAY": 3,
}

anxiety_test = Test(
    name="Anxiety Test",
    prompt="Over the last 2 weeks, how often have you been bothered by any of the following problems?\
        \nPlease note, all fields are required.",
    scores=[
        TestScore(score=(0, 4), result="Minimal Anxiety"),
        TestScore(score=(5, 9), result="Mild Anxiety"),
        TestScore(score=(10, 14), result="Moderate Anxiety"),
        TestScore(score=(15, 21), result="Severe Anxiety"),
    ],
    content={
        1: TestQuestion(
            question="Feeling nervous, anxious, or on edge",
            options=options,
        ),
        2: TestQuestion(
            question="Not being able to stop or control worrying",
            options=options,
        ),
        3: TestQuestion(
            question="Worrying too much about different things",
            options=options,
        ),
        4: TestQuestion(
            question="Trouble relaxing",
            options=options,
        ),
        5: TestQuestion(
            question="Being so restless that it is hard to sit still",
            options=options,
        ),
        6: TestQuestion(
            question="Becoming easily annoyed or irritable",
            options=options,
        ),
        7: TestQuestion(
            question="Feeling afraid as if something awful might happen",
            options=options,
        ),
    },
)
