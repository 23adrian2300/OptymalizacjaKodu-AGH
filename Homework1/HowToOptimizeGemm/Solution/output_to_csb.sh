for f in ./output_MMult*.m; do
    echo "Converting $f"
    f_csv="${f%.*}.csv"
    echo "Size: m = n = k, GFLOPS" > $f_csv
    cat $f | tail -n +3 | sed '$d' | awk 'NF{NF-=1};1' | sed -r 's/ /,/g' >> $f_csv
    echo "Saved as $f_csv"
done