from models.schemas import Test, TestQuestion, TestScore

options = {
    "NOT AT ALL": 0,
    "SEVERAL DAYS": 1,
    "MORE THAN HALF THE DAYS": 2,
    "NEARLY EVERY DAY": 3,
}

depression_test = Test(
    name="Depression Test",
    prompt="Over the last 2 weeks, how often have you been bothered by any of the following problems?\
        \nPlease note, all fields are required.",
    scores=[
        TestScore(score=(1, 4), result="Minimal Depression"),
        TestScore(score=(5, 9), result="Mild Depression"),
        TestScore(score=(10, 14), result="Moderate Depression"),
        TestScore(score=(15, 19), result="Moderately Severe Depression"),
        TestScore(score=(20, 27), result="Severe Depression"),
    ],
    content={
        1: TestQuestion(
            question="Little interest or pleasure in doing things",
            options=options,
        ),
        2: TestQuestion(
            question="Feeling down, depressed, or hopeless",
            options=options,
        ),
        3: TestQuestion(
            question="Trouble falling or staying asleep, or sleeping too much",
            options=options,
        ),
        4: TestQuestion(
            question="Feeling tired or having little energy",
            options=options,
        ),
        5: TestQuestion(
            question="Poor appetite or overeating",
            options=options,
        ),
        6: TestQuestion(
            question="Feeling bad about yourself - or that you are a failure or have let yourself or your family down",
            options=options,
        ),
        7: TestQuestion(
            question="Trouble concentrating on things, such as reading the newspaper or watching television",
            options=options,
        ),
        8: TestQuestion(
            question="Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual",
            options=options,
        ),
        9: TestQuestion(
            question="Thoughts that you would be better off dead or of hurting yourself in some way",
            options=options,
        ),
        10: TestQuestion(
            question="If you checked off any problems, how difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?",
            options=options,
        ),
    },
)
