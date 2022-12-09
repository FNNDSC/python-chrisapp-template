from pathlib import Path

from app import parser, main


def test_main(tmp_path: Path):
    # setup example data
    inputdir = tmp_path / 'incoming'
    outputdir = tmp_path / 'outgoing'
    inputdir.mkdir()
    outputdir.mkdir()
    (inputdir / 'plaintext.txt').write_text('hello ChRIS, I am a ChRIS plugin')

    # simulate run of main function
    options = parser.parse_args(['--word', 'ChRIS', '--pattern', '*.txt'])
    main(options, inputdir, outputdir)

    # assert behavior is expected
    expected_output_file = outputdir / 'plaintext.count.txt'
    assert expected_output_file.exists()
    assert expected_output_file.read_text() == '2'
