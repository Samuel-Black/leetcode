fn main() {
    fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut longest_common_prefix: String = String::from("");
        let mut longest_common_prefix_size: usize = std::usize::MAX;
        let ref str: String = strs[0];
        for n in 1..strs.len() {
            let str_length: usize = strs[n].len();
            let mut current_prefix_length: usize = 0;
            for k in 0..str_length {
                println!("{0}, - {1}", str.chars().nth(k), strs[n].chars().nth(k));
                if str.chars().nth(k) == strs[n].chars().nth(k) && k < current_prefix_length {
                    current_prefix_length+=1;
                } else {
                    break;
                }
            }
            if current_prefix_length == 0 {
                longest_common_prefix = String::from("");
                break;
            }
        //     } else if current_prefix_length < longest_common_prefix_size || longest_common_prefix_size == std::usize::MAX {
        //         longest_common_prefix_size = current_prefix_length;
        //         longest_common_prefix = String::from(&str[..longest_common_prefix_size]);
        //     }
        }
        return longest_common_prefix;
    }
    // fn test_function() -> String {
    //     return String::from("testing string");
    // }
    let vec: Vec<String> = vec![String::from("flower"),String::from("flow"),String::from("flight")];
    // let res: String = longest_common_prefix(vec);
    println!("{0}", longest_common_prefix(vec));
}
