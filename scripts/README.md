For awk example, files are

- awk_convert_to_readable.awk
- awk_put_space.awk
- awk_sample_without_space.txt
- awk_sample_with_space.txt

and here is how to use:

`awk -f awk_convert_to_readable.awk awk_sample_with_space.txt`

and

`awk -f awk_put_space.awk awk_sample_without_space.txt | awk -f awk_convert_to_readable.awk`

Have fun!
