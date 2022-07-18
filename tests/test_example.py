from pathlib import Path

from app import parser, main, DISPLAY_TITLE


def test_main(mocker, tmp_path: Path):
    """
    Simulated test run of the app.
    """
    inputdir = tmp_path / 'incoming'
    outputdir = tmp_path / 'outgoing'
    inputdir.mkdir()
    outputdir.mkdir()

    options = parser.parse_args(['--name', 'bar'])

    mock_print = mocker.patch('builtins.print')
    main(options, inputdir, outputdir)
    mock_print.assert_called_once_with(DISPLAY_TITLE)

    expected_output_file = outputdir / 'bar.txt'
    assert expected_output_file.exists()
    assert expected_output_file.read_text() == 'did nothing successfully!'
