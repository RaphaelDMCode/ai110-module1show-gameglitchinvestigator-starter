from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# ---------------------------------------------------------------------------
# check_guess — core bug: outcome labels were reversed (guess < secret was
# returning "Too High" instead of "Too Low", and vice-versa)
# ---------------------------------------------------------------------------

class TestCheckGuess:
    def test_exact_match_is_win(self):
        outcome, _ = check_guess(50, 50)
        assert outcome == "Win"

    def test_exact_match_message(self):
        _, message = check_guess(7, 7)
        assert "Correct" in message

    # Bug regression: guess BELOW secret must be "Too Low", not "Too High"
    def test_guess_below_secret_outcome_is_too_low(self):
        outcome, _ = check_guess(40, 50)
        assert outcome == "Too Low", (
            "When guess < secret the outcome must be 'Too Low' "
            "(was 'Too High' before the fix)"
        )

    def test_guess_below_secret_hint_says_go_higher(self):
        _, message = check_guess(40, 50)
        assert "HIGHER" in message, (
            "When guess < secret the hint should tell the player to go HIGHER"
        )

    # Bug regression: guess ABOVE secret must be "Too High", not "Too Low"
    def test_guess_above_secret_outcome_is_too_high(self):
        outcome, _ = check_guess(60, 50)
        assert outcome == "Too High", (
            "When guess > secret the outcome must be 'Too High' "
            "(was 'Too Low' before the fix)"
        )

    def test_guess_above_secret_hint_says_go_lower(self):
        _, message = check_guess(60, 50)
        assert "LOWER" in message, (
            "When guess > secret the hint should tell the player to go LOWER"
        )

    # Boundary values
    def test_one_below_secret(self):
        outcome, _ = check_guess(49, 50)
        assert outcome == "Too Low"

    def test_one_above_secret(self):
        outcome, _ = check_guess(51, 50)
        assert outcome == "Too High"


# ---------------------------------------------------------------------------
# parse_guess
# ---------------------------------------------------------------------------

class TestParseGuess:
    def test_valid_integer_string(self):
        ok, value, err = parse_guess("42")
        assert ok is True
        assert value == 42
        assert err is None

    def test_float_string_truncated_to_int(self):
        ok, value, _ = parse_guess("3.9")
        assert ok is True
        assert value == 3

    def test_none_input_returns_error(self):
        ok, value, err = parse_guess(None)
        assert ok is False
        assert value is None
        assert err is not None

    def test_empty_string_returns_error(self):
        ok, _, err = parse_guess("")
        assert ok is False
        assert err is not None

    def test_non_numeric_string_returns_error(self):
        ok, _, err = parse_guess("abc")
        assert ok is False
        assert err is not None


# ---------------------------------------------------------------------------
# get_range_for_difficulty
# ---------------------------------------------------------------------------

class TestGetRangeForDifficulty:
    def test_easy_range(self):
        assert get_range_for_difficulty("Easy") == (1, 20)

    def test_normal_range(self):
        assert get_range_for_difficulty("Normal") == (1, 50)

    def test_hard_range(self):
        assert get_range_for_difficulty("Hard") == (1, 100)

    def test_unknown_difficulty_defaults_to_hard_range(self):
        assert get_range_for_difficulty("Unknown") == (1, 100)


# ---------------------------------------------------------------------------
# update_score
# ---------------------------------------------------------------------------

class TestUpdateScore:
    def test_win_on_first_attempt_gives_max_points(self):
        # attempt_number=1 → 100 - 10*1 = 90
        assert update_score(0, "Win", 1) == 90

    def test_win_score_never_drops_below_ten_points(self):
        # attempt_number=10 → 100 - 10*10 = 0, clamped to 10
        result = update_score(0, "Win", 10)
        assert result >= 10

    def test_too_low_deducts_five(self):
        assert update_score(100, "Too Low", 1) == 95

    def test_unknown_outcome_leaves_score_unchanged(self):
        assert update_score(42, "Draw", 3) == 42
