from models.schemas import Test, TestQuestion, TestScore

options = {
    "STRONGLY DISAGREE": 0,
    "DISAGREE": 1,
    "NEUTRAL": 2,
    "AGREE": 3,
    "STRONGLY AGREE": 4,
}

psychosis_test = Test(
    name="Psychosis Test",
    prompt="In the past month, have you had the following thoughts, feelings, or experiences?\
        \nDo not include experiences that occur only while under the influence of alcohol, drugs or medications that were not prescribed to you.\
            \nPlease note, all fields are required.",
    scores=[
        TestScore(score=(0, 19), result="No Signs of Psychosis"),
        TestScore(score=(20, 52), result="Mild Possibility of Psychosis"),
        TestScore(score=(53, 84), result="Severe Possibility of Psychosis"),
    ],
    content={
        1: TestQuestion(
            question="Do familiar surroundings sometimes seem strange, confusing, threatening, or unreal to you?",
            options=options,
        ),
        2: TestQuestion(
            question="Have you heard unusual sounds, such as banging, clicking, hissing, clapping, or ringing in your ears?",
            options=options,
        ),
        3: TestQuestion(
            question="Do things that you see appear different from the way they usually do?",
            options=options,
        ),
        4: TestQuestion(
            question="Have you had experiences with telepathy, psychic forces, or fortune telling?",
            options=options,
        ),
        5: TestQuestion(
            question="Have you felt that you are not in control of your own ideas or thoughts?",
            options=options,
        ),
        6: TestQuestion(
            question="Do you have difficulty getting your point across, because you ramble or go off the track a lot when you talk?",
            options=options,
        ),
        7: TestQuestion(
            question="Do you have strong feelings or beliefs about being unusually gifted or talented in some way?",
            options=options,
        ),
        8: TestQuestion(
            question="Do you feel that other people are watching you or talking about you?",
            options=options,
        ),
        9: TestQuestion(
            question="Do you sometimes get strange feelings on or just beneath your skin, like bugs crawling?",
            options=options,
        ),
        10: TestQuestion(
            question="Do you sometimes feel suddenly distracted by distant sounds that you are not normally aware of?",
            options=options,
        ),
        11: TestQuestion(
            question="Have you had the sense that some person or force is around you, although you couldn't see anyone?",
            options=options,
        ),
        12: TestQuestion(
            question="Do you worry at times that something may be wrong with your mind?",
            options=options,
        ),
        13: TestQuestion(
            question="Have you ever felt that you don't exist, the world does not exist, or that you are dead?",
            options=options,
        ),
        14: TestQuestion(
            question="Have you been confused at times whether something you experienced was real or imaginary?",
            options=options,
        ),
        15: TestQuestion(
            question="Do you hold beliefs that other people would find unusual or bizarre?",
            options=options,
        ),
        16: TestQuestion(
            question="Do you feel that parts of your body have changed in some way, or that parts of your body are working differently?",
            options=options,
        ),
        17: TestQuestion(
            question="Are your thoughts sometimes so strong that you can almost hear them?",
            options=options,
        ),
        18: TestQuestion(
            question="Do you find yourself feeling mistrustful or suspicious of other people?",
            options=options,
        ),
        19: TestQuestion(
            question="Have you seen unusual things like flashes, flames, blinding light, or geometric figures?",
            options=options,
        ),
        20: TestQuestion(
            question="Have you seen things that other people can't see or don't seem to see?",
            options=options,
        ),
        21: TestQuestion(
            question="Do people sometimes find it hard to understand what you are saying?",
            options=options,
        ),
    },
)
