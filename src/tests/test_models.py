import pytest
import textwrap
from pydantic import ValidationError
from src.models import Member, Job


class TestMember:
    @pytest.mark.parametrize(
        "name,bio",
        [
            ("David", "I am a Software Engineer in Edinburgh"),
            ("", "Someone with empty name"),
            ("Someone with empty bio", ""),
        ],
    )
    def test_can_create_member_with_name_and_bio(self, name, bio):
        member = Member(name=name, bio=bio)
        assert member.name == name
        assert member.bio == bio

    @pytest.mark.parametrize(
        "name,bio,expected_exception",
        [
            (
                None,
                "Someone without a name",
                textwrap.dedent(
                    """
                    1 validation error for Member
                    name
                      Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                """  # noqa: E501
                ),
            ),
            (
                "Someone without a bio",
                None,
                textwrap.dedent(
                    """
                    1 validation error for Member
                    bio
                      Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                """  # noqa: E501
                ),
            ),
            (
                None,
                None,
                textwrap.dedent(
                    """
                    2 validation errors for Member
                    name
                      Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                    bio
                      Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                """  # noqa: E501
                ),
            ),
            (
                3,
                3,
                textwrap.dedent(
                    """
                    2 validation errors for Member
                    name
                      Input should be a valid string [type=string_type, input_value=3, input_type=int]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                    bio
                      Input should be a valid string [type=string_type, input_value=3, input_type=int]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                """  # noqa: E501
                ),
            ),
        ],
    )
    def test_can_cannot_create_member_with_non_string_args(
        self, name, bio, expected_exception
    ):
        with pytest.raises(ValidationError) as validation_error:
            Member(name=name, bio=bio)
        assert str(validation_error.value).strip() == expected_exception.strip()


class TestJob:
    @pytest.mark.parametrize(
        "title,location",
        [
            ("Software Developer", "Edinburgh"),
            ("", "Edinburgh"),
            ("Software Developer", ""),
        ],
    )
    def test_can_create_job_with_title_and_location(self, title, location):
        job = Job(title=title, location=location)
        assert job.title == title
        assert job.location == location

    @pytest.mark.parametrize(
        "title,location,expected_exception",
        [
            (
                None,
                "Job without a title",
                textwrap.dedent(
                    """
                    1 validation error for Job
                    title
                      Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                """  # noqa: E501
                ),
            ),
            (
                "Job without a location",
                None,
                textwrap.dedent(
                    """
                    1 validation error for Job
                    location
                      Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                """  # noqa: E501
                ),
            ),
            (
                None,
                None,
                textwrap.dedent(
                    """
                    2 validation errors for Job
                    title
                      Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                    location
                      Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                """  # noqa: E501
                ),
            ),
            (
                3,
                3,
                textwrap.dedent(
                    """
                    2 validation errors for Job
                    title
                      Input should be a valid string [type=string_type, input_value=3, input_type=int]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                    location
                      Input should be a valid string [type=string_type, input_value=3, input_type=int]
                        For further information visit https://errors.pydantic.dev/2.5/v/string_type
                """  # noqa: E501
                ),
            ),
        ],
    )
    def test_can_cannot_create_member_with_non_string_args(
        self, title, location, expected_exception
    ):
        with pytest.raises(ValidationError) as validation_error:
            Job(title=title, location=location)
        assert str(validation_error.value).strip() == expected_exception.strip()
