def binary_to_hexdump(input_filename, output_filename, bytes_per_line=16):
    with open(input_filename, 'rb') as f_in, open(output_filename, 'w') as f_out:
        while True:
            chunk = f_in.read(bytes_per_line)
            if not chunk:
                break
            # Convert bytes to hex with '0x' prefix and separate with commas
            hex_bytes = ', '.join(f'0x{byte:02x}' for byte in chunk)
            # Write formatted hexdump line to output file
            f_out.write(f'{hex_bytes},\n')

# Usage example
binary_to_hexdump('finch.bin', 'finch_hexdump.txt')
