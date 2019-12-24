find . -type d -exec sh -c "fc=\$(find '{}' -type f | wc -l); echo -e \"\$fc\t{}\"" \; | sort -nr
