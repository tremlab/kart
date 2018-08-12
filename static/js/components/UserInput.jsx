import React from 'react';
import $ from 'jquery';
import Kart from './Kart.jsx';
import Suggestions from './Suggestions.jsx';

class UserInput extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			userInput: '',
			kart: [],
			suggestions: []
		};

		this.handleInputAdd = this.handleInputAdd.bind(this);
		this.handleInputChange = this.handleInputChange.bind(this);
	}

	componentDidMount() {
		// gets cart from server to check if an exisitng list is in the user's session.
		$.get(window.location.href + 'kart', (data) => {
			this.setState({ kart: data })
		});
	}

	handleInputAdd(event) {
		// passes current input to server for processing into session kart.
		// then empties input field on form.
		event.preventDefault();
		const uInput = this.state.userInput
		console.log('adding...', uInput)

		if (uInput) {
			$.post(window.location.href + 'kartItem', {"userInput": uInput}, (data) => {
					this.setState({ kart: data })
			  });

			this.setState({
				userInput: ''
			});
		}
	}

	handleInputChange(event) {
		// gets from server an array of potential matches for the user's input so far
		// and updates suggestions in state.
		const value = event.target.value;
		this.setState({
			userInput: value
		});
		$.get(window.location.href + 'suggestions?userInput=' + value, (data) => {
				this.setState({ suggestions: data })
			});
	}

	render() {
		return (
			<div>
				<Suggestions suggestions={this.state.suggestions}/>
				<form className="Form">
					<input placeholder="start typing...." list="suggestions" type="text" value={this.state.userInput} onChange={this.handleInputChange} />
					<button onClick={this.handleInputAdd}>Add</button>
				</form>
				<Kart kart={this.state.kart}/>
			</div>
		);
	}
}


export default UserInput;
