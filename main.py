import wer_levenstein_engine as wle

# -----Things to discuss-----
# 8bit error
# super sonic speed speech error
# distorted (increased speed / echo) speech results are better than normal one

# if you're bored try to provide parameter True to the engine -> wle.engine(directory, True)

directory = "./test_cases_data"
wle.engine(directory, True)
