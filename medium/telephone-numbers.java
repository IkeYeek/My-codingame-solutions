import java.util.*;
import java.io.*;
import java.math.*;


class Tree {
	List<Tree> childrens;
	char value;
	
	Tree() {
		childrens = new ArrayList<>();   
	}
	
	Tree(char value) {
		childrens = new ArrayList<>();
		
		this.value = value;
	}
	
	Tree adopt(Tree child) {
		if(!childrens.stream().anyMatch(e -> (e.value == child.value))) {
			childrens.add(child);      
		}            
		Optional<Tree> node = childrens.stream().filter(e -> {
			return e.value == child.value; 
		}).findFirst();
		if(!node.isPresent())
			throw new RuntimeException("whoops cpu fucked up");
		return node.get();

	}
	
	boolean is_leaf() {
		return (childrens.size() == 0);
	}
}
class Solution {

	static int count_nodes(Tree node) {
		int total = 0;
		if(node.is_leaf()) {
			return 0;   
		} else {
			for(Tree child : node.childrens) {
				total += count_nodes(child) + 1;
			}
		}
		return total;
	}

	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		List<String> telephones = new ArrayList<String>();
		int N = in.nextInt();
		for (int i = 0; i < N; i++) {
			telephones.add(in.next());
		}
		Collections.sort(telephones);
		
		Tree root = new Tree();
		
		for(String telephone : telephones) {
			char[] telephone_chars = telephone.toCharArray();
			Tree last_node = root;
			for(int i = 0; i < telephone_chars.length; i++) {
				last_node = last_node.adopt(new Tree(telephone_chars[i]));
			}
		}
		
		int nb_nodes = count_nodes(root);
		
		
		
		System.out.println(nb_nodes);
		
	}
}